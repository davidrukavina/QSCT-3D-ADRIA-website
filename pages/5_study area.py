from pathlib import Path
from PIL import Image
import streamlit as st
import webbrowser

st.title("Adriatic foreland basin")


st.write("Thrust belts bounded basin: to the west by the Apennine thrust belt and to the east by the Dinarides-Albanides thrust-belt. During the Cenozoic the development of the Alpine and Dinaric thrust belts provided a huge sediments influx in the basin and the deposition of thick clastic sequences.")
st.write("Adriatic foreland map:")

if "homepage.py" in locals():
    current_dir = Path("homepage.py").parent
else:
    current_dir = Path.cwd()


st.write("https://github.com/davidrukavina/QSCT-3D-ADRIA-website/blob/master/qgis2web/qgis2web_2024_06_10-17_51_15_151576/index.html#7/44.351/15.886")

