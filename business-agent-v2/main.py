from core.browser import Browser
from core.files import initialize_directories
from core.logger import Logger

from engines.discovery import DiscoveryEngine
from engines.navigation import NavigationEngine


def main():

    initialize_directories()

    Logger.success("Business Agent v2")

    browser = Browser()

    driver = browser.start()

    url = input("\nWebsite: ").strip()

    if not url.startswith("http"):
        url = "https://" + url

    Logger.info(f"Opening {url}")

    driver.get(url)

    discovery = DiscoveryEngine(driver)
    discovery.scan()

    navigator = NavigationEngine(driver)

    report = navigator.analyze()

    Logger.success(f"Discovered {len(report['links'])} links")
    Logger.success("Website Intelligence Complete")

    input("\nPress ENTER to close browser...")

    browser.stop()


if __name__ == "__main__":
    main()
