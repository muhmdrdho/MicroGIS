import streamlit as st

def set_page():
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
