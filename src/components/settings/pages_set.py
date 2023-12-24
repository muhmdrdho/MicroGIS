import streamlit as st

st.set_page_config(layout='wide')

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
    #Sidebar
sidebar_setting = st.markdown(
                                    """
                                    <style>
                                        .css-1fkbmr9 {
                                                    background-color: rgb(245, 245, 245);
                                                    background-attachment: fixed;
                                                    flex-shrink: 0;
                                                    height: calc(100vh - 2px);
                                                    top: 0px;
                                                    width: 15rem;
                                                    z-index: 999991;
                                                    margin-left: 0px;
                                                    }
                                    </style>
                                    """,
                                    unsafe_allow_html=True,
                                )