from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.logger import Logger


class UniversalLoginAgent:

    def __init__(self, driver, memory):

        self.driver = driver
        self.memory = memory

    def wait_for_dashboard(self):

        Logger.info("Waiting for successful login...")

        # Wait until we're no longer on the original login page
        WebDriverWait(self.driver, 60).until(
            lambda d: d.current_url != self.memory["url"]
        )

        Logger.info("Waiting for LeadSimple application...")

        # Wait until the OAuth redirect is finished
        WebDriverWait(self.driver, 120).until(
            lambda d:
                d.execute_script("return document.readyState") == "complete"
                and d.execute_script("return document.body !== null")
                and "/v2" in d.current_url
                and "response_type=" not in d.current_url
        )

        Logger.success("Login successful")

    def login(self, username, password):

        auth = self.memory["authentication"]

        email = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(
                (By.ID, auth["email"])
            )
        )

        email.clear()
        email.send_keys(username)

        password_box = self.driver.find_element(
            By.ID,
            auth["password"]
        )

        password_box.clear()
        password_box.send_keys(password)

        self.driver.find_element(
            By.ID,
            auth["submit"]
        ).click()

        Logger.success("Credentials submitted")

        self.wait_for_dashboard()

        return True
