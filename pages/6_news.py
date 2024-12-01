import streamlit as st
from pathlib import Path
from PIL import Image
import os

video1 = open("Images/QSCT_video_1.mp4", "rb")

if "homepage.py" in locals():
    current_dir = Path("homepage.py").parent
else:
    current_dir = Path.cwd()

#---load assets---
img1=Image.open(current_dir /"Images" / "GFD_photo.jpg")
img2=Image.open(current_dir/"Images"/"HRZZ-eng.jpg")
img3=Image.open(current_dir/"Images"/"x.jpg")
img5=Image.open(current_dir/"Images"/"Project logocolor.jpg")


st.logo(img5, link="https://x.com/DaveRukavina", icon_image=img5)
st.html("""
  <style>
    [alt=Logo] {
      height: 10rem;
    }
  </style>
        """)

st.title("News")
st.write("---")



st.write("1.10.2024.")

# Path to the .jpg image (local or URL)
image_path = "C:/Users/drukavina/Documents/QSCT-3D-ADRIA/Website/Webapp/Images/x.jpg"  # Replace with your image URL or local path

# HTML code for the image button
html_button = f"""
<a href="https://x.com/DaveRukavina" target="_blank">
    <img src="{image_path}" alt="X account active" style="border: none; width: 400px; height: auto;">
</a>
"""

# Display the button using st.markdown
st.markdown(html_button, unsafe_allow_html=True)
st.write("---")


st.write("18.10.2024.")
st.write("Geophysical Fluid Dynamics group photo")
st.image(img1)
st.write("---")

st.write("22.11.2024.")
st.write("First successful modeling results. The video illustrates one of the modeled interactions between sediment supply, sea level change and tectonic subsidence. You can move the video player to speed up the sedimentation or go back in time.")
st.video(video1)
st.write("---")

st.write("29.11.2024.")
st.subheader("Pleased to announce the positive evaluation of the first period of the Croatian Science Foundation (HRZZ) scholarship.")
st.image(img2)