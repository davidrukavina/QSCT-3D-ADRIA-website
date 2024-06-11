from pathlib import Path
import os
from PIL import Image
import streamlit as st


st.set_page_config(
    page_title="Multipage App",
    page_icon=":)"
)

st.title("QSCT-3D-ADRIA - site is under construction")
st.sidebar.success("Select a page above.")

if "homepage.py" in locals():
    current_dir = Path("homepage.py").parent
else:
    current_dir = Path.cwd()


#---load assets---
img=Image.open(current_dir /"Images" / "Layout_2.jpg")
img2=Image.open(current_dir /"Images"/"RGNf samologo.jpg")
img3=Image.open(current_dir /"Images"/"HRZZ-eng.jpg")


#---HRZZ research project---

st.write("---")
image_column, text_column = st.columns((1,2))
with image_column:
    st.image(img3)

with text_column: 
    st.subheader("Outgoing mobility program project")

st.title("Quantifying the links between Sedimentation, Climatic variations and Tectonics: 3D numerical modelling and comparison with observations from the Adriatic region")
st.write("#")
st.image(img)
st.write("#")

#---collaboration---
st.write("---")
st.write("Collaboration:")
image_column, text_column = st.columns((1,2))
with image_column:
    st.image(img2)

with text_column: 
    st.write("University of Zagreb, Faculty of Mining, Geology and Petroleum Engineering")
    st.write("#")
    st.write("#")
    st.write("Geophysical Fluid Dynamics Group, Department of Earth Sciences at ETH Zürich")



