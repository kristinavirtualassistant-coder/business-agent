from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

from config import FIREFOX_BINARY, GECKODRIVER


class Browser:

    def start(self):

        options = Options()
        options.binary_location = FIREFOX_BINARY

        service = Service(executable_path=GECKODRIVER)

        driver = webdriver.Firefox(
            service=service,
            options=options
        )

        driver.maximize_window()

        return driver
