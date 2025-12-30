import streamlit as st

st.set_page_config(page_title="AI Ethics Checklist", layout="centered")

st.title("AI Ethics Checklist")
st.write("Welcome — this app is running correctly.")

principles = [
    "Fairness & Bias",
    "Transparency & Explainability",
    "Privacy & Data Protection",
    "Accountability & Governance",
    "Safety & Robustness",
]

for p in principles:
    st.checkbox(p)

st.success("🎉 Your Streamlit app is working.")
