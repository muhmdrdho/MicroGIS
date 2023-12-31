import streamlit as st
import streamlit_authenticator as stauth
from src.database.db import sign_up, fetch_users
import streamlit_antd_components as sac 
from src.components.navigation.navigation import nav
import time


def logPart():
    
    
    info, info1 = st.columns(2)
    
    users = fetch_users()
    emails = []
    usernames = []
    passwords = []

    for user in users:
        emails.append(user['key'])
        usernames.append(user['username'])
        passwords.append(user['password'])

    credentials = {'usernames': {}}
    for index in range(len(emails)):
        credentials['usernames'][usernames[index]] = {'name': emails[index], 'password': passwords[index]}

    Authenticator = stauth.Authenticate(credentials, cookie_name='Streamlit', key='abcdef', cookie_expiry_days=4)
        
        
    email, authentication_status, username = Authenticator.login(':green[Login]', 'main')

        
    if not authentication_status:
        on = st.toggle('SignUp')
        if on:
            sign_up()

    if username:
        if username in usernames:
            if authentication_status:

                    # let User see app
                st.sidebar.image('src/components/assets/microgis-logo-01.png', width=200)
                st.sidebar.subheader(f'Welcome {username}')
                    
                Authenticator.logout('Log Out', 'sidebar')
                    
                sidebar_navigation = nav()
                    

            elif not authentication_status:
                with info:
                    st.error('Incorrect Password or username')
            else:
                with info:
                    st.warning('Please feed in your credentials')
        else:
            with info:
                st.warning('Username does not exist, Please Sign up')


    