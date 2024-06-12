from pathlib import Path
from PIL import Image
import streamlit as st
import webbrowser
import requests
from lxml import etree






st.write("Thrust belts bounded basin: to the west by the Apennine thrust belt and to the east by the Dinarides-Albanides thrust-belt. During the Cenozoic the development of the Alpine and Dinaric thrust belts provided a huge sediments influx in the basin and the deposition of thick clastic sequences.")
st.write("Adriatic foreland map:")

if "homepage.py" in locals():
    current_dir = Path("homepage.py").parent
else:
    current_dir = Path.cwd()

# Step 1: Define the URL of the raw HTML file
url = "https://raw.githubusercontent.com/davidrukavina/QSCT-3D-ADRIA-website/master/qgis2web/qgis2web_2024_06_10-17_51_15_151576/index.html"

# Step 2: Fetch the content from the URL
response = requests.get(url)
response.raise_for_status() # Raise an error if the request fails

html_content = response.text
tree = etree.HTML(html_content)
title = tree.xpath("//title/text/()")
print(title[0] if title else "No title found")


