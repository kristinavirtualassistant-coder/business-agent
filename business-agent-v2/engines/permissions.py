import time
from pathlib import Path

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from config import (
    HTML_DIR,
    SCREENSHOT_DIR
)

from core.logger import Logger
from core.utils import timestamp


class PermissionEngine:

    def __init__(self, driver):
        self.driver = driver

    def discover(self):

        Logger.info("Waiting for authenticated dashboard...")

        # Wait until we're actually on the application.
        WebDriverWait(self.driver, 60).until(
            lambda d: "/v2" in d.current_url
        )

        # Wait until the document reports fully loaded.
        WebDriverWait(self.driver, 60).until(
            lambda d: d.execute_script(
                "return document.readyState"
            ) == "complete"
        )

        # Give React a few seconds to finish rendering.
        time.sleep(5)

        ts = timestamp()

        html_file = Path(HTML_DIR) / f"dashboard_{ts}.html"
        screenshot_file = Path(SCREENSHOT_DIR) / f"dashboard_{ts}.png"

        html_file.write_text(
            self.driver.page_source,
            encoding="utf-8"
        )

        self.driver.save_screenshot(str(screenshot_file))

        Logger.success(
            f"Dashboard HTML saved: {html_file.name}"
        )

        Logger.success(
            f"Dashboard Screenshot saved: {screenshot_file.name}"
        )

        Logger.info(f"URL: {self.driver.current_url}")
        Logger.info(f"Title: {self.driver.title}")

        ready_state = self.driver.execute_script(
            "return document.readyState"
        )

        Logger.info(f"Ready State: {ready_state}")

        root_length = self.driver.execute_script("""
            const root = document.getElementById('root');
            return root ? root.innerHTML.length : -1;
        """)

        Logger.info(f"Root HTML length: {root_length}")

        body_length = self.driver.execute_script("""
            return document.body.innerText.length;
        """)

        Logger.info(f"Body text length: {body_length}")

        js_anchor_count = self.driver.execute_script("""
            return document.querySelectorAll("a").length;
        """)

        js_button_count = self.driver.execute_script("""
            return document.querySelectorAll("button").length;
        """)

        Logger.info(f"JS anchor count: {js_anchor_count}")
        Logger.info(f"JS button count: {js_button_count}")

        anchors = self.driver.find_elements(By.TAG_NAME, "a")
        buttons = self.driver.find_elements(By.TAG_NAME, "button")

        Logger.info(f"Selenium anchor count: {len(anchors)}")
        Logger.info(f"Selenium button count: {len(buttons)}")

        sidebar = []
        top_navigation = []
        pages = []

        seen = set()

        for link in anchors:

            text = (link.text or "").strip()
            href = link.get_attribute("href") or ""

            if not text:
                continue

            if text in seen:
                continue

            seen.add(text)

            sidebar.append(text)

            pages.append({
                "name": text,
                "url": href
            })

        for button in buttons:

            text = (button.text or "").strip()

            if text:
                top_navigation.append(text)

        permissions = sorted(
            list(
                set(
                    sidebar +
                    top_navigation
                )
            )
        )

        Logger.success(
            f"Discovered {len(permissions)} permissions."
        )

        return {
            "logged_in": True,
            "software": self.detect_software(),
            "workspace": self.driver.title,
            "sidebar": sidebar,
            "top_navigation": top_navigation,
            "pages": pages,
            "permissions": permissions
        }

    def detect_software(self):

        title = self.driver.title.lower()

        if "leadsimple" in title:
            return "LeadSimple"

        return self.driver.title
