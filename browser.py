from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

from config import (
    FIREFOX_BINARY,
    GECKODRIVER,
    HEADLESS,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    PAGE_LOAD_TIMEOUT,
)


class Browser:

    def start(self):

        options = Options()
        options.binary_location = FIREFOX_BINARY

        if HEADLESS:
            options.add_argument("--headless")

        service = Service(executable_path=GECKODRIVER)

        driver = webdriver.Firefox(
            service=service,
            options=options
        )

        driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
        driver.set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)

        return driver
