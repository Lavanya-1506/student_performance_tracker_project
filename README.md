# Student Performance Tracker Project Report 

# Intern Details
Intern ID: [CITS2184]

Full Name: Lavanya Vaidya

No. of Weeks: 4 Weeks

Project Name: AI Student Performance Tracker

Domain: Machine Learning

# Project Overview
A Student Performance Analysis System is a machine learning–based application that analyzes student academic and behavioral data to evaluate, monitor, and predict student performance.

The main goal of the system is to help students, teachers, and institutions understand the factors affecting academic performance and provide insights for improvement.

**Project Objective**

The project collects various student-related parameters such as:

-Study hours

-Attendance

-Previous marks

-Assignment completion

-Internet usage

-Participation in activities


Using this data, the system:

-Tracks student progress

-Analyzes learning patterns

-Predicts future performance

-Identifies weak areas

-Provides improvement suggestions


## Features

- **Predictive Analytics**: Predict student performance scores (0-100) and grades (A-F)
- **Personalized Suggestions**: Get actionable recommendations based on individual student data
- **Interactive Dashboard**: Real-time visualizations and analytics
- **Multiple ML Models**: Linear Regression, Decision Tree, Random Forest, XGBoost
- **RESTful API**: Easy integration with other systems
- **Responsive Design**: Works on desktop, tablet, and mobile devices


## 📊 Factors Considered

- Study hours per day
- Attendance percentage
- Previous marks
- Assignment completion rate
- Sleep hours
- Participation in activities
- Internet usage
- Parent education level

# System Architecture

┌─────────────────────────────────────────────────────────────────┐
│                    STUDENT PERFORMANCE ANALYZER                  │
│                        SYSTEM ARCHITECTURE                       │
└─────────────────────────────────────────────────────────────────┘

                              ┌─────────────┐
                              │   USER      │
                              │ (Student/   │
                              │  Teacher)   │
                              └──────┬──────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────┐
│                         FRONTEND (Browser)                      │
├─────────────────────────────────────────────────────────────────┤
│  • Input Form (8 parameters)                                    │
│  • Submit Button                                                │
│  • Results Display                                              │
│  • Charts & Visualizations                                      │
│  • Suggestions Section                                          │
└────────────────────────────┬────────────────────────────────────┘
                             │ HTTP POST/GET
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                     BACKEND API (Flask)                         │
├─────────────────────────────────────────────────────────────────┤
│  Endpoints:                                                     │
│  • /api/predict - POST predictions                              │
│  • /api/analysis - GET analysis report                          │
│  • /api/save_student - POST save records                        │
│  • /api/performance_stats - GET statistics                      │
└────────────┬──────────────────────────────────┬────────────────┘
             │                                  │
             ▼                                  ▼
┌────────────────────────┐        ┌────────────────────────────┐
│   ML MODEL PREDICTION  │        │   DATA PROCESSING          │
├────────────────────────┤        ├────────────────────────────┤
│ 1. Load trained model  │        │ 1. Validate input          │
│ 2. Scale features      │        │ 2. Format data             │
│ 3. Predict score       │        │ 3. Generate suggestions    │
│ 4. Determine grade     │        │ 4. Prepare response        │
└────────────┬───────────┘        └────────────┬───────────────┘
             │                                 │
             └──────────────┬──────────────────┘
                            ▼
              ┌─────────────────────────┐
              │   RESPONSE TO FRONTEND  │
              ├─────────────────────────┤
              │ • Predicted Score       │
              │ • Grade (A-F)           │
              │ • Suggestions (Array)   │
              │ • Analysis Data         │
              └─────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    DATA FLOW DIAGRAM                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Raw Data ──► Preprocessing ──► EDA ──► Model Training          │
│     │              │              │             │               │
│     ▼              ▼              ▼             ▼               │
│  CSV File     Clean Data      Visuals      Trained Model        │
│                                                      │          │
│                                                      ▼          │
│  User Input ──────────────────────────────► Prediction          │
│      │                                              │           │
│      ▼                                              ▼           │
│  Validate                                        Result         │
│      │                                              │           │
│      ▼                                              ▼           │
│  Transform                                   Suggestions        │
│                                                   │             │
│                                                   ▼             │
│                                              Final Output       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    MODEL PIPELINE                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Input Features (8)                                             │
│       │                                                         │
│       ▼                                                         │
│  StandardScaler ──────────────────────────────┐                 │
│       │                                        │                │
│       ├──► Linear Regression ────┐            │                 │
│       ├──► Decision Tree ────────┤            │                 │
│       ├──► Random Forest ────────┼──► Compare ──► Best Model    │
│       └──► XGBoost ──────────────┘            │                 │
│                                                ▼                │
│                                           Save Model            │
│                                                │                │
│                                                ▼                │
│  New Student Data ──────────────────────► Prediction            │
│                                                │                │
│                                                ▼                │
│                                      Performance Score + Grade  │
│                                                │                │
│                                                ▼                │
│                                      Recommendation Engine      │
│                                                │                │
│                                                ▼                │
│                                          Suggestions            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

# Tech Stack

**Frontend** | HTML5 | CSS3 | JavaScript | User interface |
**Styling** | Bootstrap 5 | Responsive design |
**Visualization** | Chart.js | Interactive charts |
**Backend** | Flask (Python) | API server |
**ML Framework** | Scikit-learn | Model training |
**Boosting** | XGBoost | Advanced predictions |
**Data Processing** | Pandas, NumPy | Data manipulation |
**Model Serialization** | Joblib | Save/load models |


