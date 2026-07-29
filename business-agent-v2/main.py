from core.browser import Browser
from core.files import initialize_directories
from core.logger import Logger

from engines.discovery import DiscoveryEngine
from engines.navigation import NavigationEngine
from engines.memory import MemoryEngine
from engines.permissions import PermissionEngine
from engines.recovery import RecoveryEngine

from plugins.leadsimple.login import UniversalLoginAgent

from config import (
    LEADSIMPLE_EMAIL,
    LEADSIMPLE_PASSWORD,
)


def main():

    initialize_directories()

    Logger.section("Business Agent v2")

    browser = Browser()
    driver = browser.start()

    recovery = RecoveryEngine()

    url = input("\nWebsite: ").strip()

    if not url.startswith("http"):
        url = "https://" + url

    Logger.info(f"Opening {url}")

    recovery.retry(lambda: driver.get(url))

    discovery = DiscoveryEngine(driver)
    discovery.scan()

    navigator = NavigationEngine(driver)
    navigator.analyze()

    memory_engine = MemoryEngine()
    memory = memory_engine.load()

    if memory["page_type"] == "login":

        Logger.success("Login page detected.")

        login = UniversalLoginAgent(
            driver,
            memory
        )

        login.login(
            LEADSIMPLE_EMAIL,
            LEADSIMPLE_PASSWORD
        )

        Logger.success("Agent authenticated.")

        permission_engine = PermissionEngine(driver)

        permissions = permission_engine.discover()

        memory_engine.save_permissions(permissions)

        Logger.success(
            f"Learned {len(permissions['permissions'])} permissions."
        )

    else:

        Logger.warning("No login required.")

    input("\nPress ENTER to close browser...")

    browser.stop()


if __name__ == "__main__":
    main()
