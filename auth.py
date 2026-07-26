from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import (
    LEADSIMPLE_EMAIL,
    LEADSIMPLE_PASSWORD,
    LOGIN_URL,
    DASHBOARD_URL,
)


def login(driver):

    wait = WebDriverWait(driver, 60)

    driver.get(LOGIN_URL)

    email = wait.until(
        EC.visibility_of_element_located((By.ID, "email-address"))
    )

    email.clear()
    email.send_keys(LEADSIMPLE_EMAIL)

    password = driver.find_element(By.ID, "password")
    password.clear()
    password.send_keys(LEADSIMPLE_PASSWORD)

    driver.find_element(By.ID, "login-btn").click()

    print("Logging in...")

    wait.until(
        EC.presence_of_element_located((By.ID, "root"))
    )

    print("✓ Login successful")

    driver.get(DASHBOARD_URL)

    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[data-testid="task-list-item"]')
        )
    )

    print("✓ Tasks loaded")
