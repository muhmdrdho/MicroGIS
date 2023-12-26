
import streamlit as st
from streamlit_option_menu import option_menu

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