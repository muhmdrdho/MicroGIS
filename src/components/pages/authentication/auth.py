import streamlit as st
from deta import Deta


project = Deta(st.secrets['deta_key'])

actual_email = 'email'
actual_password = 'password'


placeholder = st.empty()

with placeholder.form('login'):
    email = st.text_input('email')
    password = st.text_input('password', type='password')
    submit = st.form_submit_button('Login')

if submit and email == actual_email and actual_password == actual_password:
    placeholder.empty()
    st.success('Login Successful')
elif submit and email != actual_email and password != actual_password:
    st.error('Login Failed')
else:
    pass