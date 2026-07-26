import os

from config import (
    LOG_DIR,
    HTML_DIR,
    SCREENSHOT_DIR,
    DOWNLOAD_DIR,
    MEMORY_DIR
)


def initialize_directories():

    directories = [
        LOG_DIR,
        HTML_DIR,
        SCREENSHOT_DIR,
        DOWNLOAD_DIR,
        MEMORY_DIR
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)
