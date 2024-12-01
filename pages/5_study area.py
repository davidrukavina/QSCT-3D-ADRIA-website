from pathlib import Path
from PIL import Image
import streamlit as st
import webbrowser
import requests
import os
import streamlit.components.v1 as components


if "homepage.py" in locals():
    current_dir = Path("homepage.py").parent
else:
    current_dir = Path.cwd()

#---load assets---
img=Image.open(current_dir /"Images" / "Komiza.jpg")
img1=Image.open(current_dir /"Images" / "Tectonic map.jpg")
img2=Image.open(current_dir /"Images" / "Carboni P4.jpg")
img3=Image.open(current_dir /"Images" / "Sealevels.jpg")
img5=Image.open(current_dir/"Images"/"Project logocolor.jpg")


st.logo(img5, icon_image=img5)
st.html("""
  <style>
    [alt=Logo] {
      height: 10rem;
    }
  </style>
        """)

st.subheader("Geological setting")

st.write("Interactive map:")
st.write("https://davidrukavina.github.io/QSCT-3D-ADRIA-map/")

st.write("Study area is located in the central and southern part of the Adritic foreland basin bounded by the: Apennine thrust-belt to the west and Dinarides-Albanides thrust-belt to the east (Figure 1). During the Cenozoic the development of the Alpine and Dinaric thrust belts provided a huge sediments influx in the basin and the deposition of thick clastic sequences.")
st.write("The focus of the research is on the progradation of the Pliocene to Recent sedimentary succession towards the southern Adriatic foredeep. This succession is characterized by a vertical shoaling-up succession from Pliocene deep-water and shelf deposits to Pleistocene deltaic and nearshore strata, and continuous deep-water sedimentation in foredeep. Coastal deposition during the Late Pleistocene was characterized by aeolian and alluvial deposits driven by glacial processes in the Dinaric Mountains. From the Pliocene sedimentation is characterized by several superimposed processes:")
st.write("- regional tectonic movements of the Adriatic plate between the shortening in the Dinaric Mountains and the Apennines,")
st.write("- halokinectic deformation evidenced by diapir structures (Figure 2 and 3),")
st.write("- local variations in basin subsidence and uplift (Figure 3),")
st.write("- different systems of sediment routing and (Figure 3)")
st.write("- strong climatic variations (Figure 4).")
st.write("Understanding the interaction of these processes it the main goal of this project.")



st.image(img1)
st.write("Figure 1: Tectonic map of the western Mediterranean with the most important Cenozoic structures (from Le Berton et al., 2017).")
st.write("#")
st.write("#")
st.image(img)
st.write("Figure 2: Geological map of the islands of Vis and Biševo, with a view of the bay of Komiža, which lies on the diapir structure.")
st.write("#")
st.image(img2)
st.write("Figure 3: Seismic section near the island of Palagruža presented with different attribute color bars (from Carboni et al., 2024). Here you can see examples of the diapir structure and the sediments in the subsurface.")
st.write("#")
st.image(img3)
st.write("Figure 4: Sea levels from Hansen et al. (2013) compared with ice sheet model results of de Boer et al., (2010) in (b) and in (c) with sea-level analysis of Rohling et al., (2009).")
st.write("#")
st.write("References:")
st.write("Borović, I., Marinčić, S., Majcen, Ž., Rafaeli, P., Mamužić, P., Korolija, B., Jagačić, T., Brkić, M., Grimani, I. (1975): OSNOVNA GEOLOŠKA KARTA SFRJ, List VIS (JABUKA, SVETAC, BIŠEVO), INSTITUT ZA GEOLOŠKA ISTRAŽIVANJA ZAGREB, SAVEZNI GEOLOŠKI ZAVOD BEOGRAD)")
st.write("de Boer B, Van de Wal Bintanja R, Lourens LJ, Tuetter E. (2010): Cenozoic global ice-volume and temperature simulations with 1-D ice-sheet models forced by benthic δ18Orecords. Ann.Glaciol. 51, 23–33. (doi:10.3189/172756410791392736)")
st.write("Hansen J, Sato M, Russell G, Kharecha P. (2013): Climate sensitivity, sea level and atmospheric carbon dioxide. Phil Trans R Soc A 371: 20120294. http://dx.doi.org/10.1098/rsta.2012.0294")
st.write("Le Breton, E., Handy, M. R., Molli, G., & Ustaszewski, K. (2017): Post-20 Ma motion of the Adriatic plate: New constraints from surrounding Orogens and implications for crust-mantle decoupling. Tectonics, 36, 3135–3154. https://doi.org/10.1002/2016TC004443")
st.write("Rohling EJ, Grant K, Bolshaw M, Roberts AP, Siddall M, Hemleben C, Kucera M. (2009): Antarctic temperature and global sea level closely coupled over the past ﬁve glacial cycles. Nat. Geosci. 2, 500–504. (doi:10.1038/ngeo557)")
st.write("F. Carboni, F. Mirabella, G. Minelli, H. Saleh, M. Porreca, M. Ercoli, C. Pauselli, M.R. Barchi, (2024): Kinematic reconstruction of active tectonic and halokinetic structures in the 2021 NW Palagruža earthquake area (Central Adriatic), Journal of Structural Geology, Volume 182, 105112, ISSN 0191-8141, https://doi.org/10.1016/j.jsg.2024.105112.")    


