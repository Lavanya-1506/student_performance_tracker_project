StudentPerformanceAnalyzer/
│
├── data/                      # Dataset directory
│   ├── student_records.csv
│   └── student_performance.csv # Main dataset
│
├── notebooks/                 # Jupyter notebooks
│   ├── data_preprocess_eda.ipynb
│   └── model_training.py
│
├── models/                    # Saved models
│   ├── best_model.pkl         # Trained model
│   ├── scaler.pkl            # Feature scaler
│   └── feature_columns.pkl   # Feature names
│
├── backend/                   # Flask backend
│   └── app.py                # Main application
│
├── frontend/                 # HTML templates
│   └── index.html            # Main page
│
├── static/                    # Static files
│   ├── score_distribution.png
│   ├── correlations.png
│   ├── heatmap.png
│   └── feature_importance.png
│
├── requirements.txt           # Dependencies
└── README.md                 # Documentation