import streamlit as st
from PIL import Image

choice = st.radio(label="Select how you would like to input an image, and we'll grayscale it for you!", options=['Select file', 'Camera'])

if choice == 'Select file':
    camera_image = st.file_uploader(label='Select a file')

elif choice == 'Camera':

    #Create streamlit image type
    camera_image = st.camera_input("Camera")

if camera_image:
    #Create instance of PIL image
    img = Image.open(camera_image)

    #Convert to grayscale
    gray_img = img.convert("L")

    st.image(gray_img)