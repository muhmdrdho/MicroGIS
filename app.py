import streamlit as st
import streamlit_authenticator as stauth 

import database as db


users = db.fetch_all_users()



