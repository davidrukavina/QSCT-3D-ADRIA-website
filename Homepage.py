from pathlib import Path
import os
from PIL import Image
import streamlit as st
import requests

import logging






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
img2=Image.open(current_dir /"Images"/"Logo_ETH_UZ_RGN.jpg")
img3=Image.open(current_dir /"Images"/"HRZZ-eng.jpg")
img4=Image.open(current_dir/"Images"/"vis geopark.jpg")


#---suported by---
st.write("---")
st.write("Supported by:")
image_column, text_column=st.columns((1,2))
with image_column:
    st.image(img4)

with text_column:
    st.write("part of the European and Global UNESCO Geopark Netwoks")

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
    st.subheader("University of Zagreb, Faculty of Mining, Geology and Petroleum Engineering")

    st.subheader("Geophysical Fluid Dynamics Group, Department of Earth Sciences at ETH Zürich")



