from browser import Browser
from auth import login
from navigator import Navigator


class LeadSimpleAgent:

    def __init__(self):

        self.browser = Browser()

        self.driver = None

    def run(self):

        self.driver = self.browser.start()

        login(self.driver)

        nav = Navigator(self.driver)

        nav.print_tasks()

        input("\nPress ENTER to open first contact...")

        nav.open_task(0)

        input("\nPress ENTER to quit...")
