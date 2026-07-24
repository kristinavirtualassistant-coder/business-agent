from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def inspect_page(driver):
    wait = WebDriverWait(driver, 30)

    # Wait until React finishes rendering
    wait.until(
        lambda d: d.execute_script(
            "return document.querySelector('#root')?.innerText.length > 100"
        )
    )

    print("=" * 80)
    print("TITLE")
    print(driver.title)

    print("=" * 80)
    print("URL")
    print(driver.current_url)

    print("=" * 80)
    print("LINKS")

    links = driver.find_elements(By.TAG_NAME, "a")

    for i, link in enumerate(links):
        try:
            print(
                i,
                link.text,
                link.get_attribute("href")
            )
        except:
            pass

    print("=" * 80)
    print("BUTTONS")

    buttons = driver.find_elements(By.TAG_NAME, "button")

    for i, button in enumerate(buttons):
        try:
            print(
                i,
                button.text,
                button.get_attribute("aria-label"),
                button.is_enabled()
            )
        except:
            pass
