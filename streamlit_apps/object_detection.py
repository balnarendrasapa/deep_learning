import streamlit as st
from deepface import DeepFace

def app():
    st.set_page_config(page_title="Face Recognition App Using Deepface")
    st.header("Upload an image")
    image = st.file_uploader("Choose an image...", type=["jpg", "png"])
    model = st.selectbox()
    if image != None:
        with open("image.jpg", "wb") as f:
            f.write(image.getbuffer())
        st.image(image)
        k = DeepFace.analyze(img_path="image.jpg", actions=["age", "gender"])
        st.write(k)

app()