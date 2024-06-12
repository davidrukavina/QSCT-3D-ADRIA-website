from pathlib import Path
from PIL import Image
import streamlit as st
import webbrowser
import requests
import os
import streamlit.components.v1 as components


st.title("Adraitic foreland basin")

st.write("Thrust belts bounded basin: to the west by the Apennine thrust belt and to the east by the Dinarides-Albanides thrust-belt. During the Cenozoic the development of the Alpine and Dinaric thrust belts provided a huge sediments influx in the basin and the deposition of thick clastic sequences.")
st.write("Adriatic foreland map:")

if "homepage.py" in locals():
    current_dir = Path("homepage.py").parent
else:
    current_dir = Path.cwd()


path = current_dir /'qgis2web'/'qgis2web_2024_06_10-17_51_15_151576'/'index.html'

with open (path, 'r') as f:
    html_data = f.read()

components.html(html_data)


    



