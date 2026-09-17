from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(driver, email, password):
    wait = WebDriverWait(driver, 20)

    if "/v2" in driver.current_url:
        print("Already logged in.")
        return

    print("Logging into application...")

    email_box = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='email']"))
    )
    email_box.clear()
    email_box.send_keys(email)

    password_box = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password']"))
    )
    password_box.clear()
    password_box.send_keys(password)

    login_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    login_button.click()

    print("Complete any MFA or approval flow if prompted.")
    input("Press ENTER once the app has finished loading...")
