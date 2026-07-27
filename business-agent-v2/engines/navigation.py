from selenium.webdriver.common.by import By

from core.logger import Logger


class NavigationEngine:

    def __init__(self, driver):
        self.driver = driver

    def analyze(self):

        Logger.info("Analyzing navigation...")

        report = {
            "title": self.driver.title,
            "url": self.driver.current_url,
            "menus": self.get_navigation(),
            "breadcrumbs": self.get_breadcrumbs(),
            "links": self.get_links(),
            "primary_actions": self.get_primary_actions()
        }

        Logger.success(f"Menus: {len(report['menus'])}")
        Logger.success(f"Links: {len(report['links'])}")
        Logger.success(f"Primary Actions: {len(report['primary_actions'])}")

        return report

    def get_navigation(self):

        menus = []

        for nav in self.driver.find_elements(By.TAG_NAME, "nav"):

            menus.append({
                "text": nav.text,
                "links": len(nav.find_elements(By.TAG_NAME, "a"))
            })

        return menus

    def get_breadcrumbs(self):

        crumbs = []

        selectors = [
            '[aria-label="breadcrumb"]',
            '.breadcrumb',
            '#breadcrumb'
        ]

        for selector in selectors:

            try:

                for item in self.driver.find_elements(By.CSS_SELECTOR, selector):

                    crumbs.append(item.text)

            except Exception:

                pass

        return crumbs

    def get_links(self):

        links = []

        for link in self.driver.find_elements(By.TAG_NAME, "a"):

            href = link.get_attribute("href")

            text = link.text.strip()

            links.append({
                "text": text,
                "href": href
            })

        return links

    def get_primary_actions(self):

        actions = []

        keywords = [
            "login",
            "log in",
            "sign in",
            "submit",
            "save",
            "next",
            "continue",
            "create",
            "add",
            "search",
            "start"
        ]

        for button in self.driver.find_elements(By.TAG_NAME, "button"):

            text = button.text.strip()

            if any(word in text.lower() for word in keywords):

                actions.append({
                    "text": text,
                    "id": button.get_attribute("id")
                })

        return actions
