import streamlit as st 
import streamlit_antd_components as sac 
from src.components.settings.pages_set import *
import src.components.pages.dashboard.dashboard as dsh

def nav():
    with st.sidebar:
        selected = sac.menu([
            sac.MenuItem(
                label='Dashboard',
                icon='cast'
            ),
            sac.MenuItem(
                label='explore',
                icon='compass',
                children=[
                    sac.MenuItem(
                        label='Database',
                        icon='database'
                    )
                ]
            ),
            sac.MenuItem(
                label='About',
                icon='question-circle',
                children=[
                    sac.MenuItem(
                        label='How it works?',
                        icon='gear'
                    )
                ]
            ),
        ], format_func='title', open_all=True)

    if selected =='Dashboard':
        st.header('Dashboard')
    elif selected =='Database':
        st.write('its database')
    elif selected =='How it works?':
        st.write('its works?')

    return nav

