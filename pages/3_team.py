from PIL import Image
import streamlit as st
from pathlib import Path


if "homepage.py" in locals():
    current_dir = Path("homepage.py").parent
else:
    current_dir = Path.cwd()

img5=Image.open(current_dir/"Images"/"Project logocolor.jpg")

st.logo(img5, link="https://x.com/DaveRukavina", icon_image=img5)
st.html("""
  <style>
    [alt=Logo] {
      height: 10rem;
    }
  </style>
        """)


st.title("Team")

st.write("Postdoc reasercher and project leader: Phd David Rukavina")
st.write("Project supervision: [Dr. Attila Balázs](https://balatt.weebly.com/)")
st.write("Mentor from mobility user organization: [Assoc. Prof. Bruno Saftić, PhD](https://www.rgn.unizg.hr/en/employee?djelatnik=bruno-saftic)")
st.write("User organization: University of Zagreb, [Faculy of Mining, Geology and Petroleum Engineering](https://www.rgn.unizg.hr/en/)")
st.write("Host organization: [Geophysical Fluid Dynamics](https://gfd.ethz.ch/), [Department of Earth Sciences](https://erdw.ethz.ch/en/), ETH Zurich")



