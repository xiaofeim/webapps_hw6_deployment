# from django.test import TestCase,LiveServerTestCase
# from selenium import webdriver
# from django.contrib.auth.models import User
# from manageUsers.models import Employee
# from selenium.webdriver.support.ui import Select
# import time

# class MagTestCase(LiveServerTestCase):
#     def setUp(self):
#         self.selenium = webdriver.Chrome()
#         super(MagTestCase, self).setUp()
#     def test_manage_emps_mags(self):
#         selenium = self.selenium
#         selenium.get('http://127.0.0.1:8000/')
#         # Log-in as the Manager role
#         selenium.find_element_by_id("login").click()
#         selenium.find_element_by_id("id_username").send_keys("MagSeleniumTest")
#         selenium.find_element_by_id("id_password").send_keys("MagSeleniumTest")
#         selenium.find_element_by_id("login_submit").click()
#         # Test create, edit and delete employee
#         # Add a new employee
#         selenium.find_element_by_id("manageEmployee").click()
#         selenium.find_element_by_id("add_employee").click()
#         selenium.find_element_by_id("id_e_name").send_keys("EmpSeleniumTest")
#         selenium.find_element_by_id("btn_add").click()
#         # Edit a employee
#         selenium.find_element_by_xpath(".//*[@id='emp_table']/tbody/tr[3]/td[4]/a[@id='edit_employee']").click()
#         selenium.find_element_by_id("btn_add").click()
#         # Remove the working location
#         selenium.find_element_by_xpath(".//*[@id='emp_table']/tbody/tr[3]/td[4]/a[@id='edit_res']").click()
#         selenium.find_element_by_xpath(".//*[@id='res_emp']/option[1]").click()
#         selenium.find_element_by_id("btn_add").click()
#         time.sleep(3)
#         selenium.find_element_by_id("dashboard_emp").click()
#         time.sleep(3)
#         # Test create, edit and delete manager
#         # Add a new manager
#         selenium.find_element_by_id("manageManager").click()
#         selenium.find_element_by_id("add_manager").click()
#         selenium.find_element_by_id("id_m_name").send_keys("EmpSeleniumTest")
#         selenium.find_element_by_id("btn_add").click()
#         # Edit a manager
#         selenium.find_element_by_xpath(".//*[@id='mag_table']/tbody/tr[4]/td[4]/a[@id='edit_manager']").click()
#         selenium.find_element_by_xpath(".//*[@id='edit_res_mag']/option[1]").click()
#         selenium.find_element_by_id("submit_msg").click()
#         time.sleep(3)
#         # Remove the working location
#         selenium.find_element_by_xpath(".//*[@id='mag_table']/tbody/tr[4]/td[4]/a[@id='remove_store_manager']").click()
#         selenium.find_element_by_xpath(".//*[@id='res_mag']/option[1]").click()
#         selenium.find_element_by_id("rem_btn").click()
#         # Delete the manager
#         selenium.find_element_by_xpath(".//*[@id='mag_table']/tbody/tr[4]/td[4]/a[@id='delete_manager']").click()
#         time.sleep(3)
#         selenium.find_element_by_id("dashboard_mag").click()
#         time.sleep(3)
#         selenium.quit()



