# Importing libraries that we need
import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="Graduate Employability Predictor",
    page_icon="🎓",
    layout="centered",
)

st.markdown("""
    <style>
        /* Background gradient */
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(to bottom right, #004242, #000000);
        }
        /* Center and style the main title */
        .main-title {
            text-align: center;
            font-size: 2.2em;
            font-weight: 700;
            color: #2c3e50;
        }
        /* Section title */
        .section-title {
            color: #1a237e;
            font-size: 1.3em;
            margin-top: 20px;
        }
        /* Buttons */
        div.stButton > button {
            background-color: #1565c0;
            color: white;
            border-radius: 12px;
            font-size: 1.1em;
            font-weight: 600;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            background-color: #1e88e5;
            transform: scale(1.03);
        }
        /* Success & error box styling */
        .stAlert {
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Loading our trained model
model_path = "best_employability_model.pkl"  
model = joblib.load(model_path)

st.set_page_config(page_title="Graduate Employability Predictor", page_icon="🎓", layout="centered")

# App title
st.title("🎓 Graduate Employability Predictor")
st.write("Use this app to predict whether a graduate is likely to get **placed** based on your academic and skill data.")

st.markdown("---")

# Input fields 
col1, col2 = st.columns(2)

with col1:
    iq = st.number_input("🧠 IQ Score", min_value=50, max_value=200, value=100)
    prev_result = st.number_input("📚 Previous Semester Result (%)", min_value=0.0, max_value=100.0, value=75.0)
    cgpa = st.number_input("🎓 CGPA", min_value=0.0, max_value=11.0, value=7.5)
    academic_perf = st.number_input("🏅 Academic Performance Score", min_value=0, max_value=10, value=8)

with col2:
    internship = st.selectbox("💼 Internship Experience", ["Yes", "No"])
    extra_score = st.number_input("🎨 Extra-Curricular Score", min_value=1, max_value=10, value=5)
    comms = st.number_input("🗣 Communication Skills (1–10)", min_value=1, max_value=10, value=7)
    projects = st.number_input("💻 Projects Completed", min_value=0, max_value=20, value=3)

# Prediction 
if st.button("🔍 Predict Employability"):
    data = pd.DataFrame({
        "IQ": [iq],
        "Prev_Sem_Result": [prev_result],
        "CGPA": [cgpa],
        "Academic_Performance": [academic_perf],
        "Internship_Experience": [1 if internship == "Yes" else 0],
        "Extra_Curricular_Score": [extra_score],
        "Communication_Skills": [comms],
        "Projects_Completed": [projects]
    })

    prediction = model.predict(data)[0]
    proba = model.predict_proba(data)[0][1] if hasattr(model, "predict_proba") else None

    st.markdown("---")
    if prediction == 1:
        st.success(f"✅ The model predicts this graduate is **Employable / Likely to be Placed!**")
    else:
        st.error(f"❌ The model predicts this graduate is **Not Employable / Unlikely to be Placed.**")

st.markdown("---")