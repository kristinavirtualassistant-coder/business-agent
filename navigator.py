from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Navigator:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 30)

    def get_tasks(self):

        self.wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.CSS_SELECTOR,
                    '[data-testid="task-list-item"]'
                )
            )
        )

        cards = self.driver.find_elements(
            By.CSS_SELECTOR,
            '[data-testid="task-list-item"]'
        )

        tasks = []

        for card in cards:

            task = {}

            task["title"] = card.find_element(
                By.CSS_SELECTOR,
                '[data-testid="task-list-item-title"]'
            ).text

            contact = card.find_element(
                By.CSS_SELECTOR,
                "a.tss-e1i9h-parentLink"
            )

            task["contact"] = contact.text

            task["url"] = contact.get_attribute("href")

            call_button = card.find_element(
                By.XPATH,
                './/button[.//span[contains(text(),"Call")]]'
            )

            task["call_enabled"] = call_button.is_enabled()

            tasks.append(task)

        return tasks

    def print_tasks(self):

        tasks = self.get_tasks()

        print()
        print("=" * 60)
        print(f"Found {len(tasks)} task(s)")
        print("=" * 60)

        for i, task in enumerate(tasks):

            print()

            print(f"Task {i+1}")

            print("Title   :", task["title"])

            print("Contact :", task["contact"])

            print("Call    :", task["call_enabled"])

            print("URL     :", task["url"])

    def open_task(self, index=0):

        cards = self.driver.find_elements(
            By.CSS_SELECTOR,
            '[data-testid="task-list-item"]'
        )

        contact = cards[index].find_element(
            By.CSS_SELECTOR,
            "a.tss-e1i9h-parentLink"
        )

        print(f"Opening {contact.text}")

        contact.click()
