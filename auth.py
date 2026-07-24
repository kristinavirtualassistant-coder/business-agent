from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import (
    LEADSIMPLE_EMAIL,
    LEADSIMPLE_PASSWORD,
    TASKS_URL
)


def login(driver):

    wait = WebDriverWait(driver, 60)

    driver.get("https://app.leadsimple.com")

    email = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "email-address")
        )
    )

    email.clear()
    email.send_keys(LEADSIMPLE_EMAIL)

    password = driver.find_element(By.ID, "password")

    password.clear()
    password.send_keys(LEADSIMPLE_PASSWORD)

    driver.find_element(
        By.ID,
        "login-btn"
    ).click()

    print("Logging in...")

    wait.until(
        lambda d: "sign_in" not in d.current_url
    )

    driver.get(TASKS_URL)

    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[data-testid="task-list-item"]')
        )
    )

    print("✓ Login successful")
