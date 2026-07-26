import os
from dotenv import load_dotenv

load_dotenv()


APP_NAME = "Business Agent"
APP_VERSION = "2.0.0"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MEMORY_DIR = os.path.join(BASE_DIR, "memory")
LOG_DIR = os.path.join(BASE_DIR, "logs")
HTML_DIR = os.path.join(BASE_DIR, "html")
SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")
DOWNLOAD_DIR = os.path.join(BASE_DIR, "downloads")

LEADSIMPLE_EMAIL = os.getenv("LEADSIMPLE_EMAIL", "")
LEADSIMPLE_PASSWORD = os.getenv("LEADSIMPLE_PASSWORD", "")

FIREFOX_BINARY = os.getenv(
    "FIREFOX_BINARY",
    "/Applications/Firefox.app/Contents/MacOS/firefox"
)

GECKODRIVER = os.getenv("GECKODRIVER", "")

HEADLESS = False

PAGE_TIMEOUT = 60
ELEMENT_TIMEOUT = 30
