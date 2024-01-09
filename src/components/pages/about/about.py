import streamlit as st
import streamlit_antd_components as sac

def steps():
    sac.steps(
        items=[
            sac.StepsItem(title='Connect your gps', description='Make sure your devices connected'),
            sac.StepsItem(title='Choose your data and save into your device', description='data must be .gpx formated'),
            sac.StepsItem(title='Open microgis.streamlit.app', description='sign in and choose upload menu'),
            sac.StepsItem(title='Wait until done', disabled=True),
        ], direction='vertical'
    )

steps()