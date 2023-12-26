import geopandas as gpd
import streamlit as st

def upfile():
    uploaded = st.file_uploader('Upload your files here', type='gpx', accept_multiple_files=True)
    if uploaded is not None:
        data = gpd.read_file(uploaded)
        print(data)

    return upfile()