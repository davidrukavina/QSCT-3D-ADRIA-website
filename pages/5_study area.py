from pathlib import Path
from PIL import Image
import streamlit as st
import webbrowser
import requests
import os



st.write("Thrust belts bounded basin: to the west by the Apennine thrust belt and to the east by the Dinarides-Albanides thrust-belt. During the Cenozoic the development of the Alpine and Dinaric thrust belts provided a huge sediments influx in the basin and the deposition of thick clastic sequences.")
st.write("Adriatic foreland map:")

if "homepage.py" in locals():
    current_dir = Path("homepage.py").parent
else:
    current_dir = Path.cwd()
"""
# Step 1: Define the URL of the raw HTML file
url = "https://raw.githubusercontent.com/davidrukavina/QSCT-3D-ADRIA-website/master/qgis2web/qgis2web_2024_06_10-17_51_15_151576/index.html"

# Step 2: Fetch the content from the URL
response = requests.get(url)
response.raise_for_status() # Raise an error if the request fails

# save the HTML content to a local file
local_filename = "index.html"
with open(local_filename, "w", encoding="utf-8") as file:
    file.write(response.text)

if local_filename in locals():
    current_dir = Path(local_filename).parent
else:
    current_dir = Path.cwd()
"""

path = current_dir /'qgis2web'/'qgis2web_2024_06_10-17_51_15_151576'/'index.html'
webbrowser.open(f'file://{path}')

#webbrowser.open("C:/Users/drukavina/Documents/QSCT-3D-ADRIA/Website/qgis2web/qgis2web_2024_06_10-17_51_15_151576/index.html")
    



