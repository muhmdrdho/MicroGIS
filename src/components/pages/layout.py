import src.components.pages.authentication.auth as nauth
from src.components.settings.pages_set import set_page
def page_settings():
    set = set_page()
    return set

def logPage():
    log = nauth.logPart()
    return logPage