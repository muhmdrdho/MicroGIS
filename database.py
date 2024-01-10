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
 

def upload_deta(collection: str, filename: str, byteCode: bytes) -> str:
    gpxDrive = deta.Drive(collection)
    gpxData = gpxDrive.put(filename, byteCode)

    return gpxData

def get_gpx_deta_list():
    gpxFile_db = 'gpxFile_db'
    gpxDrive = deta.Drive(gpxFile_db)
    gpxData_list = gpxDrive.list(100)

    return gpxData_list['names']

def shapefile_db():
    shp_db = 'shapefile_db'
    shp_Drive = deta.Drive(shp_db)
    shp_list = shp_Drive.list(100)

    return shp_list['names']

def get_shapefile_deta_file(filename: str):
    shp_db = 'shapefile_db'
    shp_Drive = deta.Drive(shp_db)
    shp_list = shp_Drive.list(100)

    return shp_Drive.get(filename)

def get_gpx_deta_file(filename: str):
    gpxFile_db = 'gpxFile_db'
    gpxDrive = deta.Drive(gpxFile_db)
    return gpxDrive.get(filename)

def delete_file(filename: str):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print(f"The file {filename} does not exist")

def convert_file_to_shp(source: str, output: str) -> str:
    gdf = gpd.read_file(source)
    gdf.to_file(output)
    return output

def upload_maps():
    uploaded = st.file_uploader('Choose your file', accept_multiple_files=True)
    for uploads in uploaded:

        gpxData = upload_deta("gpxFile_db", uploads.name, uploads.getvalue())

    
    data_list = get_gpx_deta_list()
    choose_data = st.selectbox("Select data", data_list)
    comp_data = get_gpx_deta_file(choose_data)
    binary_data = comp_data.read()

    fileName = choose_data
    with open(fileName, "wb") as binary_file:
        # Write bytes to file
        binary_file.write(binary_data)
    
    extractedFileName = f"extract_{fileName}"
    jsonFile = GeoJsonTransformer(fileName).save_geojson(filepath=extractedFileName)
    
    filezz, ext = fileName.split('.')
    


    with open(fileName, "rb") as file:
        # Write bytes to file
        output = file.read()
        extracted = upload_deta("JsonFile_db", jsonFile.name, output)

    #read_csv = json.load(jsonFile)
    
    

    delete_file(fileName)

    shp = convert_file_to_shp(jsonFile.name, filezz + ".shp")
    delete_file(jsonFile.name)

    m = folium.Map(tiles='OpenTopoMap')
   

     # writing files to a zipfile 
    with ZipFile(f'{filezz}.zip','w') as zip: 
        # writing each file one by one 
        files = [f'{filezz}.shp', f'{filezz}.cpg', f'{filezz}.dbf', f'{filezz}.prj', f'{filezz}.shx']
        for file in files: 
            zip.write(file)

    for file in files:
        delete_file(file)

    
    # upload zip
    with open(f'{filezz}.zip', "rb") as file:
        # Write bytes to file
        output = file.read()
        upload_deta("shpFile_db", f'{filezz}.zip', output)

    data_list1 = shapefile_db()

    read_shp = st.selectbox('select', data_list1)
    fileName1 = read_shp
    with open(fileName1, "wb") as binary_file:
        # Write bytes to file
        binary_file.write(binary_data)

    m = folium.Map(tiles='OpenTopoMap')
    folium.GeoJson(fileName1)
    

    delete_file(f'{filezz}.zip')

    
    

    


    

    

upload_maps()
