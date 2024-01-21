
import streamlit as st
import src.components.pages.authentication.auth as nauth
#from src.components.settings.pages_set import set_page

st.set_page_config('MicroGIS', menu_items=None)
#def page_settings():
    #set = set_page()
    #return set

def logPage():
    log = nauth.logPart()
    return logPage

hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
st.markdown(hide_st_style, unsafe_allow_html=True)

reduce_header_height_style = """
                <style>
                    div.block-container {padding-top:0rem;}
                </style>
            """
st.markdown(reduce_header_height_style, unsafe_allow_html=True)
