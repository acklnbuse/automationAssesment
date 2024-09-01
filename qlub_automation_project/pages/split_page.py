from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from qlub_automation_project.base.base_page import BasePage


class SplitPage(BasePage):
    split_bill_button = (By.XPATH, '//*[@data-qa-id="billing-split-bill"]')
    select_button = (By.CSS_SELECTOR, '#select-custom')
    custom_pay_amount_text = (By.XPATH, '//*[@id="regular"]/div[3]/div/div[1]/h2')
    custom_pay_amount_input = (By.CSS_SELECTOR, '#fullWidth')
    confirm_button = (By.XPATH, '//button[@id="split-bill"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_page_load()

    def wait_page_load(self):
        self.wait.until(ec.visibility_of_element_located(self.split_bill_button))

    def get_pay_amount_text(self):
        return WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.custom_pay_amount_text)
        ).text

    def click_split_bill_button(self):
        WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.split_bill_button)
        ).send_keys(Keys.RETURN)

    def click_select_button(self):
        WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.select_button)
        ).send_keys(Keys.RETURN)

    def click_custom_pay_amount_input(self):
        WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.custom_pay_amount_input)
        ).send_keys("10")

    def click_confirm_button(self):
        WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.confirm_button)
        ).send_keys(Keys.RETURN)
