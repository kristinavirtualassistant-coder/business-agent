import json
from pathlib import Path

from selenium.webdriver.common.by import By

from core.logger import Logger
from core.utils import timestamp

from config import (
    HTML_DIR,
    SCREENSHOT_DIR,
    MEMORY_DIR
)


class DiscoveryEngine:

    def __init__(self, driver):
        self.driver = driver

    def scan(self):

        Logger.info("Starting intelligent discovery...")

        ts = timestamp()

        html_file = Path(HTML_DIR) / f"{ts}.html"
        screenshot_file = Path(SCREENSHOT_DIR) / f"{ts}.png"

        html_file.write_text(
            self.driver.page_source,
            encoding="utf-8"
        )

        self.driver.save_screenshot(str(screenshot_file))

        page = {
            "title": self.driver.title,
            "url": self.driver.current_url,
            "page_type": self.detect_page_type(),
            "authentication": self.detect_authentication(),
            "navigation": self.detect_navigation(),
            "buttons": self.detect_buttons(),
            "inputs": self.detect_inputs(),
            "forms": self.detect_forms(),
            "tables": self.detect_tables()
        }

        memory = Path(MEMORY_DIR) / "selectors.json"

        memory.write_text(
            json.dumps(
                page,
                indent=4
            ),
            encoding="utf-8"
        )

        Logger.success(f"Title: {page['title']}")
        Logger.success(f"URL: {page['url']}")
        Logger.success(f"Page Type: {page['page_type']}")
        Logger.success(f"Memory Updated")

    def detect_page_type(self):

        url = self.driver.current_url.lower()

        title = self.driver.title.lower()

        if "login" in url or "signin" in url:
            return "login"

        if "signup" in url:
            return "signup"

        if "dashboard" in url:
            return "dashboard"

        if "pricing" in url:
            return "pricing"

        if "blog" in url:
            return "blog"

        if "login" in title:
            return "login"

        return "website"

    def detect_authentication(self):

        result = {
            "email": None,
            "password": None,
            "submit": None
        }

        for field in self.driver.find_elements(By.TAG_NAME, "input"):

            field_type = (field.get_attribute("type") or "").lower()

            if field_type == "email":

                result["email"] = {
                    "id": field.get_attribute("id"),
                    "name": field.get_attribute("name")
                }

            if field_type == "password":

                result["password"] = {
                    "id": field.get_attribute("id"),
                    "name": field.get_attribute("name")
                }

        for button in self.driver.find_elements(By.TAG_NAME, "button"):

            text = button.text.lower()

            if "log" in text or "sign" in text:

                result["submit"] = {
                    "text": button.text,
                    "id": button.get_attribute("id")
                }

        return result

    def detect_navigation(self):

        navs = []

        for nav in self.driver.find_elements(By.TAG_NAME, "nav"):

            navs.append(nav.text)

        return navs

    def detect_buttons(self):

        data = []

        for button in self.driver.find_elements(By.TAG_NAME, "button"):

            data.append({
                "text": button.text,
                "id": button.get_attribute("id"),
                "class": button.get_attribute("class")
            })

        return data

    def detect_inputs(self):

        data = []

        for field in self.driver.find_elements(By.TAG_NAME, "input"):

            data.append({
                "type": field.get_attribute("type"),
                "id": field.get_attribute("id"),
                "name": field.get_attribute("name"),
                "placeholder": field.get_attribute("placeholder")
            })

        return data

    def detect_forms(self):

        return [
            {} for _ in self.driver.find_elements(By.TAG_NAME, "form")
        ]

    def detect_tables(self):

        return [
            {} for _ in self.driver.find_elements(By.TAG_NAME, "table")
        ]
