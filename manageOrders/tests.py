from django.test import TestCase,LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


class manageOrdersTestCase(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()
        super(manageOrdersTestCase, self).setUp()
    def test_user(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/')
        # User log in as the manager role
        selenium.find_element_by_id("login").click()
        selenium.find_element_by_id("id_username").send_keys("MagSeleniumTest")
        selenium.find_element_by_id("id_password").send_keys("MagSeleniumTest")
        selenium.find_element_by_id("login_submit").click()
        # Click on View The Submitted Orders button in the dashboard
        # Test edit and delete submitted Orders function
        selenium.find_element_by_id("manageOrders").click()
        # Edit the order
        selenium.find_element_by_xpath(".//*[@id='table']/tbody/tr[1]/td[8]").click()
        selenium.find_element_by_id("id_customer_name").clear()
        selenium.find_element_by_id("id_customer_name").send_keys("SeleniumTest")
        selenium.find_element_by_id("save_sub_order").click()
        time.sleep(3)
        # Delete the order
        selenium.find_element_by_xpath(".//*[@id='table']/tbody/tr[1]/td[9]").click()
        time.sleep(3)
        selenium.find_element_by_id("dashboard_sub_orders").click()
        selenium.quit()
