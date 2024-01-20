import streamlit as st
from src.database.db import deta
from geojson_transformer import GeoJsonTransformer
from io import StringIO
import os
import geopandas as gpd
from zipfile import ZipFile 
from gpxcsv import gpxtolist, gpxtofile
import pandas as pd
from gpx_converter import Converter
import folium 
import json
import zipfile
from gpxplotter import read_gpx_file, create_folium_map, add_segment_to_map
from streamlit_folium import folium_static 

def shapefile_db():
    shp_db = 'shpFile_db'
    shp_Drive = deta.Drive(shp_db)
    shp_list = shp_Drive.list(100)

    return shp_list['names']

def get_shapefile_deta_file(filename: str):
    shp_db = 'shpFile_db'
    shp_Drive = deta.Drive(shp_db)
    shp_list = shp_Drive.list(100)

    return shp_Drive.get(filename)


data_list1 = shapefile_db()

read_shp = st.selectbox('select', data_list1)
read_shp_data = get_shapefile_deta_file(read_shp)
fileName1 = read_shp
binary_data = read_shp_data.read()
#with open(f'{fileName1}', "rb") as f:
    #st.download_button('Download Zip', f, file_name=f'{fileName1}')

#with open(fileName1, 'wb') as f :
    #f.write(binary_data)

with open(f'{fileName1}', "rb") as f:
    st.download_button('Download Zip', f, file_name=f'{fileName1}')

