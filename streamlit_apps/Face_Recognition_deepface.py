import streamlit as st
# from deepface import DeepFace

def app():
    st.set_page_config(page_title="Face Recognition App Using Deepface")
    st.header("Upload an image")
    image = st.file_uploader("Choose an image...", type=["jpg", "png"])

app()