import streamlit as st
import numpy as np
from PIL import Image
from detection.detect import detect_object


def main():
    st.title("Object detection with YOLOv4")
    img_array,filename = upload_image_ui()

    if isinstance(img_array, np.ndarray):
        detection,crop = detect_object(img_array,filename)
        st.text('detection')
        st.image(detection)
        st.text('cropped licence plate')
        st.image(crop)

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
