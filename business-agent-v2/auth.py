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
