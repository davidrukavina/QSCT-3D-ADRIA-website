from PIL import Image
import streamlit as st

st.title("Contact")

#---load assets---
img2=Image.open("C:\\Users\\drukavina\\Documents\\QSCT-3D-ADRIA\\Website\\Images\\RGNf samologo.jpg")
img3=Image.open("C:\\Users\\drukavina\\Documents\\QSCT-3D-ADRIA\\Website\\Images\\UniZg.png")

#---contact info---
st.write("david.rukavina@rgn.unizg.hr")
st.write("david.rukavina@erdw.ethz.ch")
st.write("phone CH: +41 766903343")
st.write("phone RH: +385 958933159")

st.write("---")

#---location info---
st.title("Locations")
st.write("ETH Zürich, Institut für Geophysik, Sonneggstrasse 5, 8092 Zürich, Switzerland")
st.write("University of Zagreb, Faculty of Mining, Geology and Petroleum Engineering, Pierottijeva ul. 6, 10000, Zagreb, Croatia")
