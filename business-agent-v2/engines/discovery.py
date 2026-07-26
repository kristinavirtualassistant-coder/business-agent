from pathlib import Path

from core.logger import Logger
from core.utils import timestamp
from config import HTML_DIR, SCREENSHOT_DIR


class DiscoveryEngine:

    def __init__(self, driver):
        self.driver = driver

    def scan(self):

        Logger.info("Starting discovery...")

        ts = timestamp()

        html_file = Path(HTML_DIR) / f"{ts}.html"
        screenshot_file = Path(SCREENSHOT_DIR) / f"{ts}.png"

        html_file.write_text(
            self.driver.page_source,
            encoding="utf-8"
        )

        self.driver.save_screenshot(str(screenshot_file))

        Logger.success(f"Title: {self.driver.title}")
        Logger.success(f"URL: {self.driver.current_url}")
        Logger.success(f"HTML: {html_file.name}")
        Logger.success(f"Screenshot: {screenshot_file.name}")
