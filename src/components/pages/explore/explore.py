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
        
       
    
    
    map_toggle = st.toggle('Activate to see the map')
    if map_toggle:
        pre_map = folium.Map(tiles='OpenTopoMap')
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
    
            #Layer control
        folium.LayerControl().add_to(pre_map)
        
                            
            #Fullscreeen
        plugins.Fullscreen().add_to(pre_map)

            #Locate Control
        plugins.LocateControl().add_to(pre_map)
                                                    
            #Cursor Postion
        fmtr = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
        plugins.MousePosition(position='topright', separator=' | ', prefix="Mouse:",lat_formatter=fmtr, lng_formatter=fmtr).add_to(pre_map)
                                    
            #Add the draw 
        plugins.Draw(export=True, filename='data.geojson', position='topleft', draw_options=None, edit_options=None).add_to(pre_map)
                                    
            #Measure Control
        plugins.MeasureControl(position='topright', primary_length_unit='meters', secondary_length_unit='miles', primary_area_unit='sqmeters', secondary_area_unit='acres').add_to(pre_map)
        folium.GeoJson('hasil.json').add_to(pre_map)
        folium_static(pre_map, width=700)
