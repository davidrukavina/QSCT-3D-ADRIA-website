from pathlib import Path
from PIL import Image
import streamlit as st

st.set_page_config(page_title="About", layout="wide")


st.title("QSCT-3D-ADRIA")
st.write("#")

st.write("The project is carried out within the Outgoing Mobility Scholarship of the Croatian Science Foundation (HRZZ), financially supported by the NextGenerationEU program.")
st.write("[HRZZ link](https://hrzz.hr/financiranje/baza-projekata/?ID=15753#baza)")
st.write("Science system information support:")
st.write("[CroRIS](https://www.croris.hr/projekti/projekt/11828)")
st.write("#")

st.write("The project deals with stratigraphic-thermo-mechanical numerical modelling using the example of the Croatian part of the Adriatic foreland basin. The project includes the analysis of a sedimentary basin based on geological and geophysical data, where the object of research is determined by the study of Pliocene to Recent (5.3 - 0 million years) sediments in the central and southern Adriatic. The project is carried out in collaboration with the Geophysical Fluid Dynamics group of the Department of Earth Sciences at ETH Zürich.")
st.write("The project aims to transfer state-of-the-art knowledge, methods, skills and tools by applying them to the analysis of sedimentary basins, i.e. parts of the Earth's crust covered by a thick sequence of sedimentary rocks. They are of extraordinary importance as they represent the natural record of the Earth's history and are one of its most important natural resources. The project will simulate the effects of tectonics, mantle dynamics, erosion, deposition and climate variability. Thermomechanical modelling will contribute to the quantification of processes and the understanding of thermal evolution, which is important for geothermal research. Stratigraphic modelling will simulate sediment deposition and distribution, which reduces the risk of identifying subsurface and is applicable across geoenergy exploration (e.g. in determining the location of energy reservoirs or underground facilities for energy or CO2 storage). The project will lead to scientific publications in prestigious peer-reviewed international journals showing the interaction of climate change and with geodynamic processes using a new detailed reconstruction of sea level in the Adriatic Sea over the last 5.3 million years.")



if "homepage.py" in locals():
    current_dir = Path("homepage.py").parent
else:
    current_dir = Path.cwd()

#---load assets---
img=Image.open(current_dir /"Images" / "Layout_2.jpg")
st.image(img)