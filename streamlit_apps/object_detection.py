import streamlit as st
from deepface import DeepFace
from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image
import requests

def app():
    st.set_page_config(page_title="Object Detection", page_icon=":eyes:")
    option = st.selectbox("Choose an option", ["Select", "Object Detection", "Face Recognition"])
    processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50", revision="no_timm")
    model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", revision="no_timm")
    if option == "Face Recognition":
        image = st.file_uploader("Choose an image...", type=["jpg", "png"])
        if image != None:
            with open("image.jpg", "wb") as f:
                f.write(image.getbuffer())
            st.image(image)
            k = DeepFace.analyze(img_path="image.jpg", actions=["age", "gender", "race", "emotion"])
            st.write(k)

    elif option == "Object Detection":
        image = st.file_uploader("Choose an image...", type=["jpg", "png"])
        if image != None:
            with open("image.jpg", "wb") as f:
                f.write(image.getbuffer())
            image = Image.open("image.jpg")
            inputs = processor(images=image, return_tensors="pt")
            outputs = model(**inputs)
            target_sizes = torch.tensor([image.size[::-1]])
            results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]
            for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
                box = [round(i, 2) for i in box.tolist()]
                st.write(
                        f"Detected {model.config.id2label[label.item()]} with confidence "
                        f"{round(score.item(), 3)} at location {box}"
                )

app()