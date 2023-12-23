from deta import Deta  # pip install deta
from dotenv import load_dotenv  # pip install python-dotenv
import streamlit_authenticator as stauth 
import streamlit as st
# Load the environment variables

DETA_KEY = "c0eqsdzdzis_VEYmbVGCW7XZda2f4v3GPN45fY78Psbf"

# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("microgisBase")


def insert_user(username, name, password):
    """Returns the user on a successful user creation, otherwise raises and error"""
    return db.put({"key": username, "name": name, "password": password})

insert_user('pparker', 'peter parker', '123')

def fetch_all_users():
    """Returns a dict of all users"""
    res = db.fetch()
    return res.items


def get_user(username):
    """If not found, the function will return None"""
    return db.get(username)


def update_user(username, updates):
    """If the item is updated, returns None. Otherwise, an exception is raised"""
    return db.update(updates, username)


def delete_user(username):
    """Always returns None, even if the key does not exist"""
    return db.delete(username)

