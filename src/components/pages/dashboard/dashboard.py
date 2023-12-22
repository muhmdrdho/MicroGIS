import streamlit as st
import folium
from streamlit_folium import st_folium

def dash():
    m = folium.Map(
        location=[-2.69, 103.01],
        zoom_start=6
    )
    st_folium(m, width=900)

    return dash