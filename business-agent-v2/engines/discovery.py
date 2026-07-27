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

        Logger.info("Starting Website Intelligence...")

        ts = timestamp()

        html_file = Path(HTML_DIR) / f"{ts}.html"
        screenshot_file = Path(SCREENSHOT_DIR) / f"{ts}.png"

        html_file.write_text(
            self.driver.page_source,
            encoding="utf-8"
        )

        self.driver.save_screenshot(str(screenshot_file))

        intelligence = {
            "title": self.driver.title,
            "url": self.driver.current_url,
            "page_type": self.detect_page_type(),
            "confidence": self.page_confidence(),
            "authentication": self.detect_authentication(),
            "structure": self.detect_structure(),
            "navigation": self.detect_navigation(),
            "headings": self.detect_headings(),
            "buttons": self.detect_buttons(),
            "inputs": self.detect_inputs(),
            "dropdowns": self.detect_dropdowns(),
            "checkboxes": self.detect_checkboxes(),
            "radio_buttons": self.detect_radios(),
            "textareas": self.detect_textareas(),
            "forms": self.detect_forms(),
            "tables": self.detect_tables(),
            "images": self.detect_images(),
            "iframes": self.detect_iframes()
        }

        memory = Path(MEMORY_DIR) / "selectors.json"

        memory.write_text(
            json.dumps(
                intelligence,
                indent=4
            ),
            encoding="utf-8"
        )

        Logger.success("Website Intelligence Complete")

    def page_confidence(self):

        score = 50

        if self.detect_authentication()["email"]:
            score += 20

        if self.detect_authentication()["password"]:
            score += 20

        if self.detect_authentication()["submit"]:
            score += 10

        return min(score, 100)

    def detect_page_type(self):

        url = self.driver.current_url.lower()
        title = self.driver.title.lower()

        if "login" in url or "sign_in" in url:
            return "login"

        if "signup" in url:
            return "signup"

        if "dashboard" in url:
            return "dashboard"

        if "settings" in url:
            return "settings"

        if "search" in url:
            return "search"

        if "report" in url:
            return "report"

        if "login" in title:
            return "login"

        return "website"

    def detect_structure(self):

        return {
            "header": len(self.driver.find_elements(By.TAG_NAME, "header")),
            "footer": len(self.driver.find_elements(By.TAG_NAME, "footer")),
            "nav": len(self.driver.find_elements(By.TAG_NAME, "nav")),
            "aside": len(self.driver.find_elements(By.TAG_NAME, "aside")),
            "section": len(self.driver.find_elements(By.TAG_NAME, "section")),
            "article": len(self.driver.find_elements(By.TAG_NAME, "article"))
        }

    def detect_authentication(self):

        auth = {
            "email": None,
            "password": None,
            "submit": None
        }

        for field in self.driver.find_elements(By.TAG_NAME, "input"):

            field_type = (field.get_attribute("type") or "").lower()

            if field_type == "email":
                auth["email"] = field.get_attribute("id")

            if field_type == "password":
                auth["password"] = field.get_attribute("id")

        for button in self.driver.find_elements(By.TAG_NAME, "button"):

            text = button.text.lower()

            if "log" in text or "sign" in text:
                auth["submit"] = button.get_attribute("id")

        return auth

    def detect_navigation(self):
        return [x.text for x in self.driver.find_elements(By.TAG_NAME, "nav")]

    def detect_headings(self):

        data = []

        for level in range(1, 7):

            for heading in self.driver.find_elements(By.TAG_NAME, f"h{level}"):

                data.append({
                    "level": level,
                    "text": heading.text
                })

        return data

    def detect_buttons(self):

        return [
            button.text
            for button in self.driver.find_elements(By.TAG_NAME, "button")
        ]

    def detect_inputs(self):

        return [
            {
                "type": x.get_attribute("type"),
                "id": x.get_attribute("id"),
                "name": x.get_attribute("name")
            }
            for x in self.driver.find_elements(By.TAG_NAME, "input")
        ]

    def detect_dropdowns(self):
        return len(self.driver.find_elements(By.TAG_NAME, "select"))

    def detect_checkboxes(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]'))

    def detect_radios(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, 'input[type="radio"]'))

    def detect_textareas(self):
        return len(self.driver.find_elements(By.TAG_NAME, "textarea"))

    def detect_forms(self):
        return len(self.driver.find_elements(By.TAG_NAME, "form"))

    def detect_tables(self):
        return len(self.driver.find_elements(By.TAG_NAME, "table"))

    def detect_images(self):
        return len(self.driver.find_elements(By.TAG_NAME, "img"))

    def detect_iframes(self):
        return len(self.driver.find_elements(By.TAG_NAME, "iframe"))
