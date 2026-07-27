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

        WebDriverWait(self.driver, 60).until(
            lambda d: d.current_url != self.memory["url"]
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
