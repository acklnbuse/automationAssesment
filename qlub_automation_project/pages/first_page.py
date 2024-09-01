from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys

from qlub_automation_project.base.base_page import BasePage


class FirstPage(BasePage):
    pay_now_button = (By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div/div/div[2]/main/div/div/div[3]/button[1]')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_page_load()

    def wait_page_load(self):
        self.wait.until(ec.visibility_of_element_located(self.pay_now_button))

    def click_pay_now_button(self):
        WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.pay_now_button)
        ).send_keys(Keys.RETURN)