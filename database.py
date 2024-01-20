import streamlit as st
from src.database.db import deta
from geojson_transformer import GeoJsonTransformer
from io import StringIO
import os
import geopandas as gpd
from zipfile import ZipFile 

import pandas as pd

import folium 
import json
import zipfile

from streamlit_folium import folium_static 

def upload_deta(collection: str, filename: str, byteCode: bytes) -> str:
    gpxDrive = deta.Drive(collection)
    gpxData = gpxDrive.put(filename, byteCode)

    return gpxData

def get_gpx_deta_list():
    gpxFile_db = 'gpxFile_db'
    gpxDrive = deta.Drive(gpxFile_db)
    gpxData_list = gpxDrive.list(100)

    return gpxData_list['names']

def get_gpx_points_deta_list():
    gpxFilePoints_db = 'gpxFilePoints_db'
    gpxDrivePoints = deta.Drive(gpxFilePoints_db)
    gpxPointData_list = gpxDrivePoints.list(100)

    return gpxPointData_list['names']

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

def shapefile_points_db():
    shp_db = 'shpFile_points_db'
    shp_Drive = deta.Drive(shp_db)
    shp_list = shp_Drive.list(100)

    return shp_list['names']

def get_shapefile_points_deta_file(filename: str):
    shp_db = 'shpFile_points_db'
    shp_Drive = deta.Drive(shp_db)
    shp_list = shp_Drive.list(100)

    return shp_Drive.get(filename)

def get_gpx_deta_file(filename: str):
    gpxFile_db = 'gpxFile_db'
    gpxDrive = deta.Drive(gpxFile_db)
    return gpxDrive.get(filename)

def get_gpx_points_deta_file(filename: str):
    gpxFilePoints_db = 'gpxFilePoints_db'
    gpxDrivePoints = deta.Drive(gpxFilePoints_db)
    return gpxDrivePoints.get(filename)

def delete_file(filename: str):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print(f"The file {filename} does not exist")

def convert_file_to_shp(source: str, output: str) -> str:
    gdf = gpd.read_file(source)
    gdf.to_file(output)
    return output

def convert_file_to_shp_points(source: str, output: str) -> str:
    gdf_points = gpd.read_file(source)
    gdf_points_df = gpd.GeoDataFrame(gdf_points, columns=['name','geometry'])
    gdf_points_df.to_file(output, driver='Esri Shapefile')
    return output

def say():
    with st.spinner():
        st.success('Done')

def upload_maps():
    options = st.selectbox('Specify the file type', ('Points','Lines'))
    uploaded = st.file_uploader('Choose your file', accept_multiple_files=True)
    for uploads in uploaded:
        data2 = uploads.name
        

        if options == 'Lines':
            st.write('Feature activated!')

            if st.button(label='Upload', on_click=say):
        
                gpxData = upload_deta("gpxFile_db", uploads.name, uploads.getvalue())

            data_list = get_gpx_deta_list()
            choose_data = st.selectbox("Select data", data_list, disabled=True)
            comp_data = get_gpx_deta_file(choose_data)
            binary_data = comp_data.read()
            fileName = choose_data
            with open(fileName, "wb") as binary_file:
                # Write bytes to file
                binary_file.write(binary_data)
            
            
            extractedFileName = f"extract_{fileName}.json"
            jsonFile = GeoJsonTransformer(fileName).save_geojson(filepath=extractedFileName)
            
            st.write(jsonFile)

        

            filezz, ext = fileName.split('.')
            


            with open(fileName, "rb") as file:
                # Write bytes to file
                output = file.read()
                extracted = upload_deta("JsonFile_db", jsonFile.name, output)

            #read_csv = json.load(jsonFile)
            
            

            delete_file(fileName)

            shp = convert_file_to_shp(jsonFile.name, filezz + ".shp")
            delete_file(jsonFile.name)

            
        

            # writing files to a zipfile 
            with ZipFile(f'{filezz}.zip','w') as zip: 
                # writing each file one by one 
                files = [f'{filezz}.shp', f'{filezz}.cpg', f'{filezz}.dbf', f'{filezz}.prj', f'{filezz}.shx']
                for file in files: 
                    zip.write(file)

            for file in files:
                delete_file(file)

            with open(f'{filezz}.zip', "rb") as file:
            # Write bytes to file
                output = file.read()
                upload_deta("shpFile_db", f'{filezz}.zip', output)

            delete_file(f'{filezz}.zip')

        if options == 'Points':
        
                
            if st.button(label='Upload', on_click=say):
        
                gpxData = upload_deta("gpxFilePoints_db", uploads.name, uploads.getvalue())

            gpxFilePoints_db = 'gpxFilePoints_db'
            gpxDrivePoints = deta.Drive(gpxFilePoints_db)
            drv = gpxDrivePoints.list(100)

            shp_db = 'shpFile_db'
            shp_Drive = deta.Drive(shp_db)

            if uploads:
                choosen_dp = st.selectbox(f"Select Data on line", drv["names"], disabled=True)
                filezz, ext = choosen_dp.split('.')
                reads = gpxDrivePoints.get(choosen_dp)

                read3 = gpd.read_file(reads)
                gdf = gpd.GeoDataFrame(read3, columns=['name', 'geometry'])
                gdf1 = gdf.to_file(f'{filezz}.shp')


                with ZipFile(f'{filezz}.zip','w') as zip: 
                                # writing each file one by one 
                        files = [f'{filezz}.shp', f'{filezz}.cpg', f'{filezz}.dbf', f'{filezz}.prj', f'{filezz}.shx']
                        for file in files: 
                            zip.write(file)

                with open(f'{filezz}.zip', "rb") as file:
                            # Write bytes to file
                            output = file.read()
                            upload_deta("shpFile_db", f'{filezz}.zip', output)

                
                for file in files:
                    delete_file(file)
                        
                delete_file(f'{filezz}.zip')

                st.write(gdf)

            else:
                st.write("check your data first")

            

        


    

    
    # upload zip
   

    
    
    #data_list1 = shapefile_db()

    #read_shp = st.selectbox('select', data_list1)
    #fileName1 = read_shp
    #with open(f'{fileName1}', "rb") as f:
        #st.download_button('Download Zip', f, file_name=f'{fileName1}')

    #b = gpd.read_file(fileName1)
    #m = folium.Map(tiles='OpenTopoMap')
    #folium.GeoJson(b).add_to(m)

    #folium_static(m)
        # Write bytes to file
        
    
    
    

    

    
    

    


    

    

upload_maps()
