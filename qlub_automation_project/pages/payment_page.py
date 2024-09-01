import time
from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys

from qlub_automation_project.base.base_page import BasePage


class PaymentPage(BasePage):
    view_menu_button = (By.XPATH, '//*[@id="invoiceElement"]/div/div/div[1]/div[2]/button')
    custom_tip_button = (By.XPATH, '//*[@id="tip_10"]/div/div')
    tip_button = (By.XPATH, '//span[@class="MuiTypography-root MuiTypography-body1 css-1hclwqz"]')
    card_number_input = (By.XPATH, '/html[1]/body[1]')
    card_expiration_input = (By.XPATH, '//input[@id="Field-expiryInput"]')
    card_cvc_input = (By.XPATH, '//button[@name="cvc"]')
    pay_button = (By.XPATH, '//button[@type="submit"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_page_load()

    def wait_page_load(self):
        self.wait.until(ec.visibility_of_element_located(self.custom_tip_button))

    def get_view_button_text(self):
        return WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(self.view_menu_button)
        ).text

    def click_tip_button(self):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.tip_button)
        ).click()

    def click_card_number_input(self):
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(self.card_number_input)
        ).send_keys("4242424242424242")

    def click_card_expiration_input(self):
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(self.card_expiration_input)
        ).send_keys("0226")

    def click_card_cvc_input(self):
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(self.card_cvc_input)
        ).send_keys("100")

    def click_pay_button(self):
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(self.pay_button)
        ).send_keys(Keys.RETURN)

    def click_iframe(self):
        iframes = WebDriverWait(self.driver, 20).until(
            ec.presence_of_all_elements_located((By.TAG_NAME, "iframe"))
        )

        for iframe in iframes:
            self.driver.switch_to.frame(iframe)
            try:
                card_number_input = WebDriverWait(self.driver, 10).until(
                    ec.presence_of_element_located((By.NAME, "number"))
                )
                card_number_input.send_keys("4242424242424242")

                expiry_input = WebDriverWait(self.driver, 10).until(
                    ec.presence_of_element_located((By.NAME, "expiry"))
                )
                expiry_input.send_keys("0226")

                cvc_input = WebDriverWait(self.driver, 10).until(
                    ec.presence_of_element_located((By.NAME, "cvc"))
                )
                cvc_input.send_keys("100")

                break
            except:
                self.driver.switch_to.default_content()

        self.driver.switch_to.default_content()

