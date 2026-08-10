import os
import streamlit as st
import requests

st.title("🎨 AI Moodboard")

prompt = st.text_area(
    "Describe your product",
    "AI Financial Assistant for Students"
)

if st.button("Generate Moodboard"):

    response = requests.post(
        f"{os.getenv('API_BASE_URL', 'http://ai-backend:8000')}/moodboard/",
        json={
            "prompt": prompt
        }
    )

    if response.status_code == 200:

        data = response.json()

        st.success("Moodboard Generated")

        st.subheader("🎯 Style")
        st.write(data["style"])

        st.subheader("🎨 Color Palette")

        cols = st.columns(len(data["colors"]))

        for i, color in enumerate(data["colors"]):
            cols[i].markdown(
                f"""
                <div style="
                width:70px;
                height:70px;
                background:{color};
                border-radius:10px;
                border:1px solid black;">
                </div>

                <center>{color}</center>
                """,
                unsafe_allow_html=True
            )

        st.subheader("🖋 Fonts")

        for font in data["fonts"]:
            st.write("•", font)

        st.subheader("✨ Keywords")

        st.write(", ".join(data["keywords"]))

    else:
        st.error("Backend Error")