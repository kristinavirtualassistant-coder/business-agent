import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def get_task_details(driver):

    print("\n===== DEBUG PAGE TEXT =====")

    body_text = driver.find_element(
        By.TAG_NAME,
        "body"
    ).text

    print(body_text[:5000])

    print("\n===== END DEBUG =====")

    return {
        "task": "",
        "owner": "",
        "phone": "",
        "property": ""
    }



def run_call_tasks(driver):

    wait = WebDriverWait(driver, 20)

    print("Waiting for Tasks page...")

    # Find first Call task
    first_task = wait.until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR,
            "div[data-testid='task-list-item'][data-task-kind='CALL']"
        ))
    )

    print("\nFound first task:")
    print(first_task.text)
    print()


    print("Opening task...")

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        first_task
    )

    time.sleep(1)


    # Click task title
    task_title = first_task.find_element(
        By.CSS_SELECTOR,
        "[data-testid='task-list-item-title']"
    )

    driver.execute_script(
        "arguments[0].click();",
        task_title
    )

    print("Task clicked.")

    # Wait for task page to load
    time.sleep(3)


    task = get_task_details(driver)

    print("\n====================")
    print("TASK DETAILS")
    print("====================")

    print("TASK:")
    print(task["task"])

    print("\nOWNER:")
    print(task["owner"])

    print("\nPHONE:")
    print(task["phone"])

    print("\nPROPERTY:")
    print(task["property"])

    print("====================")


    input("\nPress ENTER to quit...")
