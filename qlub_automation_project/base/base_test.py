import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class BaseTest(unittest.TestCase):
    driver = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = webdriver.Chrome()
        self.errors = []
        self.driver.get('https://app-staging.qlub.cloud/qr/ae/dummy-checkout/90/_/_/1827c10c80')
        self.driver.maximize_window()

    def get_driver(self, driver):
        if driver == 'chrome':
            self.driver = webdriver.Chrome()
        return self.driver

    def finalize(self):
        if self.errors:
            error_message = "\n".join(self.errors)
            raise AssertionError(f"Soft assertion failed with the following messages: {error_message}")

    def close_browser(self):
        self.driver.quit()