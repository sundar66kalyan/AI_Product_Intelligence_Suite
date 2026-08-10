import os
import streamlit as st
import requests

st.title("🤖 Gemini AI Report")

product = st.text_input(
    "Enter Product Name",
    "Gemini"
)

if st.button("Generate Report"):

    response = requests.post(
        f"{os.getenv('API_BASE_URL', 'http://ai-backend:8000')}/gemini-report/",
        json={
            "product": product
        }
    )

    if response.status_code == 200:

        data = response.json()

        st.success("Report Generated Successfully")

        st.subheader("📋 Executive Summary")
        st.write(data["executive_summary"])

        st.subheader("✅ Strengths")
        for item in data["strengths"]:
            st.success(item)

        st.subheader("❌ Weaknesses")
        for item in data["weaknesses"]:
            st.error(item)

        st.subheader("🚀 Opportunities")
        for item in data["opportunities"]:
            st.info(item)

        st.subheader("⚠ Risks")
        for item in data["risks"]:
            st.warning(item)

        st.subheader("💡 Recommendations")
        for item in data["recommendations"]:
            st.success(item)

        st.metric("Overall Score", data["score"])

    else:
        st.error("Failed to generate report.")