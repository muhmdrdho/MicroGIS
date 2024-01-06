import streamlit as st
from geojson_transformer import GeoJsonTransformer
from io import StringIO
import os
from zipfile import ZipFile 
from src.database.db import upload_deta, get_deta_list, get_deta_file, delete_file, convert_file_to_shp 


def upload_maps():
    uploaded = st.file_uploader('Choose your file', accept_multiple_files=True)
    for uploads in uploaded:
        
        stringio = StringIO(uploads.getvalue().decode('utf-8'))
        string_data = stringio.read()

        gpxData = upload_deta("gpxFile_db", uploads.name, uploads.getvalue())

    
    data_list = get_deta_list()
    choose_data = st.selectbox("Select data to see view", data_list)
    comp_data = get_deta_file(choose_data)
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

    
    # upload zip
    with open(f'{filezz}.zip', "rb") as file:
        # Write bytes to file
        output = file.read()
        upload_deta("shpFile_db", f'{filezz}.zip', output)

    delete_file(f'{filezz}.zip')
    

    

upload_maps()
