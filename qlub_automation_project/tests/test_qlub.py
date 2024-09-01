import time
from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from qlub_automation_project.base.base_test import BaseTest
from qlub_automation_project.pages.first_page import FirstPage
from qlub_automation_project.pages.payment_page import PaymentPage
from qlub_automation_project.pages.split_page import SplitPage

class TestQlub(BaseTest):

    def test_qlub(self):
        first_page = FirstPage(self.driver)
        first_page.click_pay_now_button()
        time.sleep(5)

        split_page = SplitPage(self.driver)
        split_page.click_split_bill_button()
        split_page.click_select_button()
        split_page.click_custom_pay_amount_input()
        split_page.click_confirm_button()

        payment_page = PaymentPage(self.driver)
        payment_page.click_tip_button()
        payment_page.click_iframe()
        time.sleep(10)
        payment_page.click_pay_button()