from selenium.webdriver.common.by import By

from core.logger import Logger


class NavigationEngine:

    def __init__(self, driver):
        self.driver = driver

    def analyze(self):

        Logger.info("Analyzing page...")

        elements = {
            "links": self.driver.find_elements(By.TAG_NAME, "a"),
            "buttons": self.driver.find_elements(By.TAG_NAME, "button"),
            "inputs": self.driver.find_elements(By.TAG_NAME, "input"),
            "forms": self.driver.find_elements(By.TAG_NAME, "form"),
            "tables": self.driver.find_elements(By.TAG_NAME, "table"),
        }

        Logger.success(f"Title : {self.driver.title}")
        Logger.success(f"URL   : {self.driver.current_url}")

        Logger.success(f"Links   : {len(elements['links'])}")
        Logger.success(f"Buttons : {len(elements['buttons'])}")
        Logger.success(f"Inputs  : {len(elements['inputs'])}")
        Logger.success(f"Forms   : {len(elements['forms'])}")
        Logger.success(f"Tables  : {len(elements['tables'])}")

        return elements
