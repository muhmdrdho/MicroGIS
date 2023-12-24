import streamlit_antd_components as sac
import streamlit as st

def nav():
    with st.sidebar:
        option_menu = sac.menu([
                        sac.MenuItem('Dashboard', 
                                     icon='cast'),
                        sac.MenuItem('Explore', 
                                     icon='compass', 
                                     children=[
                                        sac.MenuItem('Database', 
                                                     icon='apple'),
                        ]),
                        sac.MenuItem('About', 
                                     icon='question-circle',
                                     children=[
                                         sac.MenuItem('How it works?',
                                                      icon='gear')
                                         
                                     ]),    
                    ], format_func='title', size='small', indent=10, open_all=True, return_index=True)
nav()