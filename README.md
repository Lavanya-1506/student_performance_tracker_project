# 🎓 AI Student Performance Tracker

## 📌 Internship Details

| Field            | Details                        |
| ---------------- | ------------------------------ |
| **Intern ID**    | CITS2184                       |
| **Intern Name**  | Lavanya Vaidya                 |
| **Duration**     | 4 Weeks                        |
| **Project Name** | AI Student Performance Tracker |
| **Domain**       | Machine Learning               |

---

# 📖 Project Overview

The **AI Student Performance Tracker** is a Machine Learning-based application designed to analyze, monitor, and predict student academic performance.

The system evaluates various academic and behavioral factors to identify performance trends, predict future outcomes, and provide personalized recommendations for improvement.

This project helps:

* 🎓 Students monitor and improve their academic performance
* 👨‍🏫 Teachers identify students who may need additional support
* 🏫 Educational institutions make data-driven decisions

---

# 🎯 Project Objectives

The system analyzes student-related factors such as:

* Study Hours
* Attendance Percentage
* Previous Marks
* Assignment Completion Rate
* Internet Usage
* Participation in Activities

Using these factors, the system can:

* Track student progress
* Analyze learning patterns
* Predict future performance
* Identify weak areas
* Generate personalized improvement suggestions

---

# ✨ Key Features

* 📊 Student Performance Prediction
* 📝 Grade Prediction (A–F)
* 📈 Performance Tracking and Analysis
* 🤖 Multiple Machine Learning Models Comparison
* 💡 Personalized Improvement Recommendations
* 📉 Exploratory Data Analysis (EDA)
* 📊 Interactive Data Visualizations
* ⚡ Real-Time Performance Prediction
* 🔗 RESTful API Integration
* 📱 Responsive User Interface

---

# 📋 Factors Considered

The prediction model considers the following parameters:

* Study Hours per Day
* Attendance Percentage
* Previous Academic Marks
* Assignment Completion Rate
* Sleep Hours
* Participation in Activities
* Internet Usage
* Parent Education Level

---

# 🔄 Project Workflow

```text
Student Data
      │
      ▼
Data Preprocessing
      │
      ▼
Exploratory Data Analysis (EDA)
      │
      ▼
Feature Engineering & Scaling
      │
      ▼
Model Training & Evaluation
      │
      ▼
Best Model Selection
      │
      ▼
Model Deployment (Flask API)
      │
      ▼
User Input
      │
      ▼
Performance Prediction
      │
      ▼
Grade Prediction & Recommendations
      │
      ▼
Results Dashboard
```

---

# 🏗️ System Architecture

```text
User Input
     │
     ▼
Frontend Interface
     │
     ▼
Flask Backend API
     │
     ▼
Data Validation & Processing
     │
     ▼
Machine Learning Model
     │
     ▼
Performance Prediction
     │
     ▼
Grade Prediction
     │
     ▼
Recommendation Engine
     │
     ▼
Results Dashboard
```

---

# 🤖 Machine Learning Models Used

The following algorithms were implemented and evaluated:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* XGBoost Regressor

The best-performing model was selected based on evaluation metrics.

---

# 📊 Model Evaluation Metrics

The model performance was evaluated using:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

---

# 🛠️ Technology Stack

| Category         | Technologies            |
| ---------------- | ----------------------- |
| Frontend         | HTML5, CSS3, JavaScript |
| Styling          | Bootstrap 5             |
| Visualization    | Chart.js                |
| Backend          | Flask (Python)          |
| Machine Learning | Scikit-learn            |
| Boosting         | XGBoost                 |
| Data Processing  | Pandas, NumPy           |
| Model Storage    | Joblib                  |

---

# 📁 Project Structure

```text
AI-Student-Performance-Tracker/
│
├── dataset/
│   └── student_data.csv
│
├── models/
│   └── trained_model.pkl
│
├── notebooks/
│   └── analysis.ipynb
│
├── backend/
│   └── app.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── requirements.txt
└── README.md
```

---

# 🚀 Future Enhancements

* Student Login & Authentication
* Teacher Dashboard
* PDF Report Generation
* Email Notifications
* Subject-wise Performance Analysis
* Attendance Management System
* AI-Based Study Recommendations
* Cloud Deployment

---

⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/yourusername/StudentPerformanceAnalyzer.git
cd StudentPerformanceAnalyzer
2. Install Dependencies
pip install -r requirements.txt
3. Generate Dataset (First Time Only)
python data/generate_dataset.py
4. Train the Model
python notebooks/model_training.py
5. Run the Application
python backend/app.py
6. Open the Application

Open your browser and navigate to:

http://localhost:5000
