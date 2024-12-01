import streamlit as st
from pathlib import Path
from PIL import Image
import os

# Checking current directory and verifying file existence
current_dir = Path.cwd()

video1_path = current_dir / "Images" / "QSCT_video_1.mp4"
img1_path = current_dir / "Images" / "GFD_photo.jpg"
img2_path = current_dir / "Images" / "HRZZ-eng.jpg"
img3_path = current_dir / "Images" / "x.jpg"
img5_path = current_dir / "Images" / "Project logocolor.jpg"

# Check if video and images exist
print("Video file exists:", os.path.exists(video1_path))
print("Image files exist:", os.path.exists(img1_path), os.path.exists(img2_path), os.path.exists(img5_path))

# Open images if files exist
if os.path.exists(img5_path):
    img5 = Image.open(img5_path)
else:
    img5 = None

if os.path.exists(img1_path):
    img1 = Image.open(img1_path)

if os.path.exists(img2_path):
    img2 = Image.open(img2_path)

if os.path.exists(img3_path):
    img3 = Image.open(img3_path)

# Display logo if img5 exists
if img5:
    st.logo(img5, icon_image=img5)
st.html("""
  <style>
    [alt=Logo] {
      height: 10rem;
    }
  </style>
        """)

# ----News title---
st.title("News")
st.write("---")



# Continue with other content
st.write("1.10.2024.")
st.write("[Active X account](https://x.com/DaveRukavina)")
if img3:
    st.image(img3)
st.write("---")

st.write("18.10.2024.")
st.write("Geophysical Fluid Dynamics group photo")
if img1:
    st.image(img1)
st.write("---")

st.write("22.11.2024.")
st.write("First successful modeling results.")

# Video display: Convert Path object to string
if os.path.exists(video1_path):
    st.video(str(video1_path))  # Convert the pathlib.Path object to a string
else:
    st.write("Video file is missing!")
st.write("---")


st.write("29.11.2014.")
st.write("pleased to announce a positive evaluation of the first period of the outgoing mobility scholarship of the Croatian Science Foundation.")
if img2:
    st.image(img2)
st.write("---")
