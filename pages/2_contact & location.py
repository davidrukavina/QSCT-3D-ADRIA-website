from pathlib import Path
from PIL import Image
import streamlit as st





if "homepage.py" in locals():
    current_dir = Path("homepage.py").parent
else:
    current_dir = Path.cwd()

#---load assets---
img2=Image.open(current_dir /"Images"/"RGNf samologo.jpg")
img3=Image.open(current_dir/"Images"/"UniZg.png")
img5=Image.open(current_dir/"Images"/"Project logocolor.jpg")


st.logo(img5, link="https://x.com/DaveRukavina", icon_image=img5)
st.html("""
  <style>
    [alt=Logo] {
      height: 10rem;
    }
  </style>
        """)

st.title("Contact")

#---contact info---
st.write("david.rukavina@rgn.unizg.hr")
st.write("david.rukavina@eaps.ethz.ch")
st.write("phone CH: +41 766903343")
st.write("phone RH: +385 958933159")

st.write("---")

#---location info---
st.title("Locations")
st.write("ETH Zürich, Institut für Geophysik, Sonneggstrasse 5, 8092 Zürich, Switzerland")
st.write("University of Zagreb, Faculty of Mining, Geology and Petroleum Engineering, Pierottijeva ul. 6, 10000, Zagreb, Croatia")
