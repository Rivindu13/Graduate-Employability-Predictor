🎓 Graduate Employability Predictor

The Graduate Employability Predictor is a machine learning–powered web application designed to estimate a graduate’s likelihood of being employed after completing their studies.
It leverages academic, personal, and skill-based data to provide an objective employability assessment.

📊 Overview

This project uses a data-driven approach to assess employability potential among undergraduates.
The model was trained on the Graduate Employability Dataset from Kaggle and integrated into an interactive Streamlit web application for real-time predictions.

The system allows users to input information such as academic performance, communication skills, project experience, and internship history — then instantly receive a prediction on whether they are likely to be employable or not.

🧠 Project Workflow

1.Data Preprocessing
  Handled missing values and outliers
  Standardized numerical features
  Encoded categorical variables
  
2.Model Training
  Evaluated multiple algorithms including:
    Logistic Regression
    Random Forest
    XGBoost
  Selected the best-performing model based on accuracy and generalization ability
  
3.Deployment
  Saved the final model as best_employability_model.pkl
  Integrated it into a Streamlit web application for interactive use

| Feature                             | Description                                          |
| ----------------------------------- | ---------------------------------------------------- |
| 🧠 **IQ**                           | Student’s intelligence quotient                      |
| 📚 **Previous Semester Result (%)** | Academic percentage in the previous semester         |
| 🎓 **CGPA**                         | Overall cumulative GPA                               |
| 🏅 **Academic Performance Score**   | Normalized performance score (0–10)                  |
| 💼 **Internship Experience**        | Whether the student completed an internship (Yes/No) |
| 🎨 **Extra-Curricular Score**       | Participation in extracurricular activities (0–10)   |
| 🗣 **Communication Skills**          | Rated on a scale of 1–10                             |
| 💻 **Projects Completed**           | Number of academic or technical projects completed   |

=======================
🚀 Technologies Used

Python 🐍
Pandas, NumPy — Data preprocessing
Scikit-learn, XGBoost — Model training
Joblib — Model serialization
Streamlit — Web app development

=======================
🎯 Purpose

This project aims to support:
  Educational institutions in identifying students who may need additional training
  Career counselors in guiding students based on measurable attributes
  Undergraduates in understanding factors that influence their employability outcomes

=======================
👨‍💻 Author

Rivindu Dulan
💡 “Empowering students with data-driven career insights.”
