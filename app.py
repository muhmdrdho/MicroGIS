import src.major as major
import streamlit as st 


hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.markdown('''
<style>
.styles_terminalButton__JBj5T{
    visibility:hidden;
}
</style>
''', unsafe_allow_html=True)

microgis = major.main_layout()