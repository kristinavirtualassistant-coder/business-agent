import os
from dotenv import load_dotenv

load_dotenv()

LEADSIMPLE_EMAIL = os.getenv("LEADSIMPLE_EMAIL")
LEADSIMPLE_PASSWORD = os.getenv("LEADSIMPLE_PASSWORD")

FIREFOX_BINARY = "/Applications/Firefox.app/Contents/MacOS/firefox"

GECKODRIVER = "/Users/kristinamacbookpro/.wdm/drivers/geckodriver/mac64/v0.37.1/geckodriver"

TASKS_URL = "https://app.leadsimple.com/v2/tasks/XcZ87w9ddFnR4OWK_sP-PzbBoflEGc4_4geNmXCHCvY=?taskType=MANUAL&dueType=UPCOMING"
