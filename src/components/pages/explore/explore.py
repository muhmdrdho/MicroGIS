import streamlit as st
from src.database.db import deta
import folium
from folium import plugins
from streamlit_folium import folium_static
import os
import json

def get_json_deta_list():
    jsonFile_db = 'JsonFile_db'
    jsonDrive = deta.Drive(jsonFile_db)
    jsonData_list = jsonDrive.list(100)

    return jsonData_list['names']

def delete_file(filename: str):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print(f"The file {filename} does not exist")

def get_json_deta_file(filename: str):
    jsonFile_db = 'JsonFile_db'
    jsonDrive = deta.Drive(jsonFile_db)
    return jsonDrive.get(filename)

def shpFile_db():
    shp_db = 'shpFile_db'
    shp_Drive = deta.Drive(shp_db)
    shp_list = shp_Drive.list(100)

    return shp_list['names']

def get_shpFile_deta_file(filename: str):
    shp_db = 'shpFile_db'
    shp_Drive = deta.Drive(shp_db)
    shp_list = shp_Drive.list(100)

    return shp_Drive.get(filename)


def explore():
    select_file = st.selectbox('Select file',('Json', 'Gpx', 'Shapefile') )
    if select_file == 'Json':
        jsonData = get_json_deta_list()
        expData = st.selectbox('select your data', jsonData)
        comp_json_data = get_json_deta_file(expData)
        binary_data = comp_json_data.read()
         
        fileName = expData
        with open(fileName, "wb") as binary_file:
                # Write bytes to file
            binary_file.write(binary_data)

    if select_file == 'Shapefile':
        shpData2 = shpFile_db()
        shpData = st.selectbox('select your data',shpData2 )
        comp_shp_data = get_shpFile_deta_file(shpData)
        data2 = comp_shp_data.read()
        shpread = shpData
        
        shp_down = st.download_button(label='Download your Shapefile', data=data2)
        
       
    
    datashp = 'hasil.json'
    map_toggle = st.toggle('Activate to see the map')
    if map_toggle:
        pre_map = folium.Map(tiles='OpenTopoMap')
        folium.GeoJson('hasil.json').add_to(pre_map)
        Esri_Satellite = folium.TileLayer(
                                                                                tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                                                                                attr = 'Esri',
                                                                                name = 'Esri Satellite',
                                                                                overlay = True,
                                                                                control = True
                                                                                ).add_to(pre_map)
        Google_Satellite_Hybrid =  folium.TileLayer(
                                                                                tiles = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
                                                                                attr = 'Google',
                                                                                name = 'Google Satellite',
                                                                                overlay = True,
                                                                                control = True
                                                                                ).add_to(pre_map)
        Google_Terrain = folium.TileLayer(
                                                                                tiles = 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
                                                                                attr = 'Google',
                                                                                name = 'Google Terrain',
                                                                                overlay = True,
                                                                                control = True
                                                                                ).add_to(pre_map)
        Google_Satellite = folium.TileLayer(
                                                                                tiles = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
                                                                                attr = 'Google',
                                                                                name = 'Google Satellite',
                                                                                overlay = True,
                                                                                control = True
                                                                                ).add_to(pre_map)
        Google_Maps = folium.TileLayer(
                                                                                tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
                                                                                attr = 'Google',
                                                                                name = 'Google Maps',
                                                                                overlay = True,
                                                                                control = True
                                                                                ).add_to(pre_map)
        folium.LayerControl().add_to(pre_map)
        folium_static(pre_map, width=700)

    
explore()