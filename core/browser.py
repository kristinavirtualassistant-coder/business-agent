from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Browser:

    def __init__(self):
        self.driver = None

    def start(self):
        options = Options()
        options.set_preference("detach", True)

        self.driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install()),
            options=options
        )

        self.driver.maximize_window()

        return self.driver

    def open(self, url):
        self.driver.get(url)

    def quit(self):
        if self.driver:
            self.driver.quit()
