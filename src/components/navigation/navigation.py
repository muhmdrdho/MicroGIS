
import streamlit as st
from streamlit_option_menu import option_menu
from src.components.pages.upload.upload import upfile

def nav():
    with st.sidebar:
        selected = option_menu(None, ["Explore", "Upload",  "About"], 
                                icons=['compass', 'cloud-upload', "list-task"], 
                                menu_icon="cast", default_index=0, orientation="vertical",
                                styles={
                                    "container": {"padding": "0!important", "background-color": "#fafafa"},
                                    "icon": {"color": "black", "font-size": "15px"}, 
                                    "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#fcd2d2"},
                                    "nav-link-selected": {"background-color": "#c42121"},
                                }
)
    if selected == "Explore":
        st.header("This is explore")

    if selected  == "Upload":
        st.header("This is Upload")
        upfile()

    if selected == "About":
        st.header("This is About")