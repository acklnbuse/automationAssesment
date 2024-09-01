from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):

    def __init__(self, driver, explicit_wait=30):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, explicit_wait)

    def driver(self):
        return self.driver