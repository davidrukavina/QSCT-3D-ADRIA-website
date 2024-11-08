import streamlit as st
from pathlib import Path
from PIL import Image

if "homepage.py" in locals():
    current_dir = Path("homepage.py").parent
else:
    current_dir = Path.cwd()

img=Image.open(current_dir /"Images" / "azu.jpg")
img2=Image.open(current_dir /"Images" / "tgs.jpg")
print(current_dir / "Images" / "azu.jpg")

st.title("Data")
st.write("Project is based on analysis and interpretation of offshore 2D seismic and well data. Seismic data represents the core of the interest since it gives the chance to understand halokinetic structures, faults, depositional surfaces and bodies in subsurface.")
st.write("#")
st.write("This project is supported by the Croatian Hydrocarbon Agency and TGS , who provided the seismic and well data from the central and southern Adriatic Sea.")
st.image(img)
st.image(img2)


st.write("---")

st.title("Softwares")
st.write("Many thanks to BeicipFranlab for providing the DionisosFlow and CougarFlow licence for Stratigraphic Modelling")
st.write("For modelling of the salt interation with sedimentation and tectonics i3ELVIS 3D thermomechanical numerical code will be used.")

