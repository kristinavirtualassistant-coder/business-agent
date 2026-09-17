import os
from dotenv import load_dotenv

load_dotenv()

APP_EMAIL = os.getenv("APP_EMAIL") or os.getenv("CRM_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD") or os.getenv("CRM_PASSWORD")
APP_URL = os.getenv("APP_URL", "https://app.example.com")
TASKS_URL = os.getenv("TASKS_URL", os.getenv("WORK_QUEUE_URL", APP_URL))

FIREFOX_BINARY = os.getenv("FIREFOX_BINARY", "/Applications/Firefox.app/Contents/MacOS/firefox")
GECKODRIVER = os.getenv("GECKODRIVER", "/Users/you/.wdm/drivers/geckodriver/mac64/v0.37.1/geckodriver")
