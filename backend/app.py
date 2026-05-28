from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import joblib
import os
import sys
from sklearn.ensemble import RandomForestRegressor

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'frontend'),
    static_folder=os.path.join(BASE_DIR, 'static')
)
CORS(app)

NO_SLEEP_FEATURE_COLUMNS = [
    'study_hours',
    'attendance_percentage',
    'previous_marks',
    'assignments_completed',
    'activity_participation',
    'internet_usage_hours'
]


def train_no_sleep_model():
    """Train a model using only fields available in the web form."""
    dataset_path = os.path.join(BASE_DIR, 'data', 'student_performance_dataset.csv')
    df = pd.read_csv(dataset_path)
    trained_model = RandomForestRegressor(
        n_estimators=300,
        random_state=42,
        min_samples_leaf=2
    )
    trained_model.fit(df[NO_SLEEP_FEATURE_COLUMNS], df['performance_score'])
    return trained_model, NO_SLEEP_FEATURE_COLUMNS


try:
    models_dir = os.path.join(BASE_DIR, 'notebooks', 'models')
    model = joblib.load(os.path.join(models_dir, 'best_model.pkl'))
    scaler = joblib.load(os.path.join(models_dir, 'scaler.pkl'))
    feature_columns = joblib.load(os.path.join(models_dir, 'feature_columns.pkl'))

    if 'sleep_hours' in feature_columns:
        model, feature_columns = train_no_sleep_model()
        scaler = None
        print("No-sleep model trained from dataset.")

    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    try:
        model, feature_columns = train_no_sleep_model()
        print("No-sleep model trained from dataset.")
    except Exception as training_error:
        print(f"Error training no-sleep model: {training_error}")
        model = None
        feature_columns = []
    scaler = None

FORM_TO_MODEL_COLUMNS = {
    'attendance_percentage': 'attendance',
    'assignments_completed': 'assignment_completion',
    'activity_participation': 'participation',
    'internet_usage_hours': 'internet_usage'
}


def build_model_input(data):
    """Convert frontend fields into the columns used during model training."""
    model_data = {}

    for column in feature_columns:
        source_column = FORM_TO_MODEL_COLUMNS.get(column, column)

        if source_column in data:
            value = data[source_column]
        else:
            raise ValueError(f"Missing required input: {source_column}")

        if column == 'assignments_completed':
            value = float(value) / 10 if float(value) > 10 else float(value)
        elif column == 'activity_participation':
            value = {0: 0, 1: 3, 2: 6, 3: 10}.get(int(value), float(value))

        model_data[column] = float(value)

    return pd.DataFrame([model_data], columns=feature_columns)


def should_scale_features():
    """Scale only models that were trained with scaled features."""
    return scaler is not None and model.__class__.__name__ not in {'XGBRegressor', 'RandomForestRegressor'}


def get_grade(score):
    """Convert numeric score to letter grade."""
    if score >= 85:
        return 'A', 'Excellent! Keep up the great work!'
    if score >= 70:
        return 'B', 'Good job! You have potential to reach A.'
    if score >= 55:
        return 'C', 'Satisfactory. Focus on improving weak areas.'
    if score >= 40:
        return 'D', 'Needs improvement. Don\'t give up!'
    return 'F', 'Requires significant improvement. Seek help!'


def get_score_range(score):
    """Return the lower and upper score bounds for the predicted grade band."""
    if score >= 85:
        return 85, 100
    if score >= 70:
        return 70, 84.99
    if score >= 55:
        return 55, 69.99
    if score >= 40:
        return 40, 54.99
    return 0, 39.99


def get_students_in_score_range(predicted_score, limit=10):
    """Find students whose actual performance score falls in the same range."""
    dataset_path = os.path.join(BASE_DIR, 'data', 'student_performance_dataset.csv')
    if not os.path.exists(dataset_path):
        return []

    df = pd.read_csv(dataset_path)
    required_columns = {'student_id', 'name', 'performance_score', 'grade'}
    if not required_columns.issubset(df.columns):
        return []

    lower_score, upper_score = get_score_range(predicted_score)
    matching_students = df[
        (df['performance_score'] >= lower_score)
        & (df['performance_score'] <= upper_score)
    ].copy()

    matching_students['score_difference'] = (
        matching_students['performance_score'] - predicted_score
    ).abs()
    matching_students = matching_students.sort_values(
        ['score_difference', 'performance_score'],
        ascending=[True, False]
    ).head(limit)

    return [
        {
            'student_id': row.student_id,
            'name': row.name,
            'performance_score': float(row.performance_score),
            'grade': row.grade
        }
        for row in matching_students.itertuples(index=False)
    ]


def generate_suggestions(student_data, predicted_score):
    """Generate personalized suggestions based on student data and prediction."""
    suggestions = []

    if student_data['study_hours'] < 5:
        suggestions.append({
            'category': 'Study Hours',
            'suggestion': f"Increase study hours from {student_data['study_hours']} to at least 6 hours/day",
            'priority': 'High',
            'impact': '+15-20 points'
        })
    elif student_data['study_hours'] < 7:
        suggestions.append({
            'category': 'Study Hours',
            'suggestion': f"Maintain {student_data['study_hours']} hours of study, try to reach 7-8 hours for better results",
            'priority': 'Medium',
            'impact': '+5-10 points'
        })

    if student_data['attendance'] < 75:
        suggestions.append({
            'category': 'Attendance',
            'suggestion': f"Improve attendance from {student_data['attendance']}% to at least 85%",
            'priority': 'High',
            'impact': '+10-15 points'
        })
    elif student_data['attendance'] < 85:
        suggestions.append({
            'category': 'Attendance',
            'suggestion': f"Good attendance ({student_data['attendance']}%), aim for 90%+",
            'priority': 'Low',
            'impact': '+3-5 points'
        })

    if student_data['assignment_completion'] < 70:
        suggestions.append({
            'category': 'Assignments',
            'suggestion': f"Complete more assignments (currently {student_data['assignment_completion']}%)",
            'priority': 'High',
            'impact': '+8-12 points'
        })

    if student_data['internet_usage'] > 6:
        suggestions.append({
            'category': 'Internet Usage',
            'suggestion': f"Reduce internet usage from {student_data['internet_usage']} to under 4 hours/day",
            'priority': 'High',
            'impact': '+10-15 points'
        })
    elif student_data['internet_usage'] > 4:
        suggestions.append({
            'category': 'Internet Usage',
            'suggestion': f"Monitor internet usage ({student_data['internet_usage']} hours/day)",
            'priority': 'Medium',
            'impact': '+5-8 points'
        })

    participation_map = {0: 'None', 1: 'Low', 2: 'Medium', 3: 'High'}
    current_participation = participation_map.get(student_data['participation'], 'Unknown')
    if student_data['participation'] < 2:
        suggestions.append({
            'category': 'Activities',
            'suggestion': f"Increase participation in extracurricular activities (currently {current_participation})",
            'priority': 'Medium',
            'impact': '+5-8 points'
        })

    if student_data['previous_marks'] < 60 and predicted_score > student_data['previous_marks']:
        suggestions.append({
            'category': 'Progress',
            'suggestion': f"Great improvement from {student_data['previous_marks']}%! Keep building on this momentum",
            'priority': 'Low',
            'impact': 'Already improving'
        })

    priority_order = {'High': 0, 'Medium': 1, 'Low': 2}
    suggestions.sort(key=lambda item: priority_order[item['priority']])

    return suggestions


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        if model is None:
            return jsonify({
                'success': False,
                'error': 'Model is not available. Please train the model or check notebooks/models.'
            }), 500

        data = request.json or {}
        features_array = build_model_input(data)

        if should_scale_features():
            features_array = scaler.transform(features_array)

        predicted_score = model.predict(features_array)[0]
        grade, grade_message = get_grade(predicted_score)
        suggestions = generate_suggestions(data, predicted_score)
        matching_students = get_students_in_score_range(predicted_score)

        return jsonify({
            'success': True,
            'predicted_score': round(float(predicted_score), 2),
            'grade': grade,
            'grade_message': grade_message,
            'suggestions': suggestions,
            'matching_students': matching_students,
            'input_data': data
        }), 200

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/api/analysis/<student_id>', methods=['GET'])
def get_analysis(student_id):
    analysis = {
        'student_id': student_id,
        'strengths': ['Good study habits', 'Regular attendance'],
        'weaknesses': ['Low assignment completion', 'High internet usage'],
        'recommendations': [
            'Complete pending assignments',
            'Reduce screen time',
            'Join study groups'
        ],
        'predicted_trend': 'Improving with current efforts'
    }
    return jsonify(analysis), 200


@app.route('/api/save_student', methods=['POST'])
def save_student():
    try:
        student_data = request.json or {}
        df = pd.DataFrame([student_data])

        records_path = os.path.join(BASE_DIR, 'data', 'student_records.csv')
        if os.path.exists(records_path):
            existing_df = pd.read_csv(records_path)
            df = pd.concat([existing_df, df], ignore_index=True)

        df.to_csv(records_path, index=False)

        return jsonify({'success': True, 'message': 'Student record saved successfully'}), 200

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/api/performance_stats', methods=['GET'])
def get_performance_stats():
    try:
        dataset_path = os.path.join(BASE_DIR, 'data', 'student_performance_dataset.csv')
        if not os.path.exists(dataset_path):
            return jsonify({'error': 'No data available'}), 404

        df = pd.read_csv(dataset_path)
        numeric_df = df.select_dtypes(include='number')

        stats = {
            'total_students': len(df),
            'average_score': float(df['performance_score'].mean()),
            'grade_distribution': df['grade'].value_counts().to_dict(),
            'best_feature_correlation': float(
                numeric_df.corr()['performance_score'].drop('performance_score').max()
            )
        }
        return jsonify(stats), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
