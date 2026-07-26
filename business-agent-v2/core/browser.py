from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

from config import (
    FIREFOX_BINARY,
    GECKODRIVER,
    HEADLESS,
    PAGE_TIMEOUT
)

from core.logger import Logger


class Browser:

    def __init__(self):
        self.driver = None

    def start(self):

        Logger.info("Starting Firefox...")

        options = Options()
        options.binary_location = FIREFOX_BINARY

        if HEADLESS:
            options.add_argument("-headless")

        service = Service(executable_path=GECKODRIVER)

        self.driver = webdriver.Firefox(
            service=service,
            options=options
        )

        self.driver.set_page_load_timeout(PAGE_TIMEOUT)
        self.driver.maximize_window()

        Logger.success("Firefox started")

        return self.driver

    def stop(self):

        if self.driver:

            Logger.info("Closing Firefox...")

            self.driver.quit()

            Logger.success("Firefox closed")
