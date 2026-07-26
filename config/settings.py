"""
Business Agent Configuration
"""

import os
from dotenv import load_dotenv

load_dotenv()

# =========================
# LOGIN
# =========================

EMAIL = os.getenv("LEADSIMPLE_EMAIL")
PASSWORD = os.getenv("LEADSIMPLE_PASSWORD")

# =========================
# URLS
# =========================

BASE_URL = "https://app.leadsimple.com"
LOGIN_URL = f"{BASE_URL}/users/sign_in"
TASKS_URL = f"{BASE_URL}/v2"

# =========================
# BROWSER
# =========================

HEADLESS = False
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900

# =========================
# TIMEOUTS
# =========================

PAGE_LOAD_TIMEOUT = 30
ELEMENT_TIMEOUT = 15
SHORT_WAIT = 2
LONG_WAIT = 5

# =========================
# DEBUG
# =========================

SAVE_SCREENSHOTS = True
SAVE_HTML = True
DEBUG = True
