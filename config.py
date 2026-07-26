import os
from dotenv import load_dotenv

load_dotenv()

# LeadSimple Credentials
LEADSIMPLE_EMAIL = os.getenv("LEADSIMPLE_EMAIL")
LEADSIMPLE_PASSWORD = os.getenv("LEADSIMPLE_PASSWORD")

# Browser
FIREFOX_BINARY = "/Applications/Firefox.app/Contents/MacOS/firefox"
GECKODRIVER = "/Users/kristinamacbookpro/.wdm/drivers/geckodriver/mac64/v0.37.1/geckodriver"

HEADLESS = False
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900
PAGE_LOAD_TIMEOUT = 30
ELEMENT_TIMEOUT = 15
SHORT_WAIT = 2
LONG_WAIT = 5

# URLs
BASE_URL = "https://app.leadsimple.com"
LOGIN_URL = "https://id.leadsimple.com/users/sign_in"
DASHBOARD_URL = "https://app.leadsimple.com/v2"

# Debug
SAVE_SCREENSHOTS = True
SAVE_HTML = True
DEBUG = True
