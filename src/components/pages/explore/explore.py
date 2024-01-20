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

def explore():
    options = st.selectbox('Select your data first', ['Gpx', 'Shapefile'])

    if options == 'Shapefile':
        st.write('This is shapefile')

        data_list = shapefile_db()
        choose_data = st.selectbox("Select data", data_list)
        comp_data = get_shapefile_deta_file(choose_data)
        binary_data = comp_data.read()
        fileName = choose_data
        with open(fileName, "wb") as binary_file:
            # Write bytes to file
            binary_file.write(binary_data)
            st.download_button('Download Zip', binary_data, file_name=f'{fileName}')
        

        read = gpd.read_file(fileName)
        gdf = gpd.GeoDataFrame(read)
        m = folium.Map(tiles='OpenTopoMap')
        folium.GeoJson(gdf).add_to(m)
        folium_static(m)


        

                
        