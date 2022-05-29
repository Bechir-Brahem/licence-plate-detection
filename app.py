import streamlit as st
import numpy as np
from PIL import Image
from detection.detect import detect_object


def main():
    st.title("Object detection with YOLOv5")
    img_array,filename = upload_image_ui()

    if isinstance(img_array, np.ndarray):
        detection,crops = detect_object(img_array,filename)
        st.text('detection')
        st.image(detection)
        for crop in crops:
            st.text('cropped licence plate:  '+crop['text'])
            st.image(crop['img'])

def upload_image_ui():
    uploaded_image = st.file_uploader("Please choose an image file", type=["png", "jpg", "jpeg"])
    if uploaded_image is not None:
        try:
            image = Image.open(uploaded_image)
        except Exception:
            st.error("Error: Invalid image")
        else:
            img_array = np.array(image)
            print(uploaded_image)
            return (img_array, uploaded_image.name)
    else :
        return None,None

if __name__ == '__main__':
    main()
