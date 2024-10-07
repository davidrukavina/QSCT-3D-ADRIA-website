from pathlib import Path
import os
from PIL import Image
import streamlit as st
import requests
from google.oauth2 import service_account
from googleapiclient.discovery import build
import logging


st.set_page_config(
    page_title="Multipage App",
    page_icon=":)"
)

st.title("QSCT-3D-ADRIA - site is under construction")
st.sidebar.success("Select a page above.")

if "homepage.py" in locals():
    current_dir = Path("homepage.py").parent
else:
    current_dir = Path.cwd()


#---load assets---
img=Image.open(current_dir /"Images" / "Layout_2.jpg")
img2=Image.open(current_dir /"Images"/"Logo_ETH_UZ_RGN.jpg")
img3=Image.open(current_dir /"Images"/"HRZZ-eng.jpg")
img4=Image.open(current_dir/"Images"/"vis geopark.jpg")


#---suported by---
st.write("---")
st.write("Supported by:")
image_column, text_column=st.columns((1,2))
with image_column:
    st.image(img4)

with text_column:
    st.write("part of the European and Global UNESCO Geopark Netwoks")

#---HRZZ research project---

st.write("---")
image_column, text_column = st.columns((1,2))
with image_column:
    st.image(img3)

with text_column: 
    st.subheader("Outgoing mobility program project")

st.title("Quantifying the links between Sedimentation, Climatic variations and Tectonics: 3D numerical modelling and comparison with observations from the Adriatic region")
st.write("#")
st.image(img)
st.write("#")

#---collaboration---
st.write("---")
st.write("Collaboration:")
image_column, text_column = st.columns((1,2))
with image_column:
    st.image(img2)

with text_column: 
    st.subheader("University of Zagreb, Faculty of Mining, Geology and Petroleum Engineering")

    st.subheader("Geophysical Fluid Dynamics Group, Department of Earth Sciences at ETH Zürich")




# Cloudflare API credentials (replace with your credentials)
CLOUDFLARE_API_TOKEN = "gnE2fp1Knn9q_SgmWVj_QorIUv8aX74k3uebQlLE"
ZONE_ID = "fd65f7d0eabc302e9b4c8f5a25fa5b84"  # Cloudflare Zone ID for your domain
DOMAIN_NAME = "https://qsct-3d-adria.streamlit.app/"  # Your custom domain

# DNS TXT record data (replace with your verification code)
dns_record = {
    "type": "TXT",
    "name": "qsct-3d-adria.streamlit.app",
    "content": "google-site-verification=cZ4kkFXL8xeyma7k5ZPPZytrlUCVB3gy-8blx1QLku4",  # Replace with your Google verification TXT value
    "ttl": 120,
    "proxied": False
}

# Cloudflare API URL to create the DNS TXT record
url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records"

# Cloudflare API headers
headers = {
    "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
    "Content-Type": "application/json"
}

# Send the request to Cloudflare API
response = requests.post(url, json=dns_record, headers=headers)

# Check response status
if response.status_code == 200:
    print("DNS TXT record added successfully!")
else:
    print(f"Failed to add DNS record: {response.status_code}")
    print(response.text)


logging.basicConfig(level=logging.INFO)

@st.cache
def load_data():
    # Log some info
    logging.info("Loading data...")
    # Your data loading code here

if __name__ == "__main__":
    logging.info("Starting Streamlit app...")
    st.title("My Streamlit App")
    load_data()