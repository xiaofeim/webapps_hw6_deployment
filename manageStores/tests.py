# from django.test import TestCase, LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from django.contrib.auth.models import User
# from .models import Restaurant
# import time
# from django.utils import timezone
# from manageItems.models import GlobalMenu


# class testStore(TestCase):
#     def test_restaurant(self):
#         global_menu = GlobalMenu.objects.create(
#             global_menu_name="TestStore", pub_date=timezone.now())
#         restaurant = Restaurant.objects.create(
#             global_menu=global_menu, restauran_location="TestRestaurant")
#         self.assertEqual("TestRestaurant", restaurant.restauran_location)


# class StoreTestCase(LiveServerTestCase):
#     def setUp(self):
#         self.selenium = webdriver.Chrome()
#         super(StoreTestCase, self).setUp()

#     def test_user(self):
#         selenium = self.selenium
#         selenium.get('http://127.0.0.1:8000/')
#         # User log in as the manager role
#         selenium.find_element_by_id("login").click()
#         selenium.find_element_by_id("id_username").send_keys("MagSeleniumTest")
#         selenium.find_element_by_id("id_password").send_keys("MagSeleniumTest")
#         selenium.find_element_by_id("login_submit").click()
#         # Click on Manage The Restaurant button in the dashboard
#         # Test add, edit and delete restaurant function
#         selenium.find_element_by_id("manageStores").click()
#         # Add the store
#         selenium.find_element_by_id("add_store").click()
#         selenium.find_element_by_id("id_global_menu").click()
#         select = Select(selenium.find_element_by_id("id_global_menu"))
#         select.select_by_visible_text("Menu")
#         time.sleep(3)
#         selenium.find_element_by_id(
#             "id_restauran_location").send_keys("6000 Centre Ave")
#         selenium.find_element_by_id("add_store").click()
#         # Edit the store
#         selenium.find_element_by_xpath(
#             ".//*[@id='table_store']/tbody/tr[5]/td[3]/a").click()
#         selenium.find_element_by_id("id_restauran_location").clear()
#         selenium.find_element_by_id(
#             "id_restauran_location").send_keys("6100 Centre Ave")
#         selenium.find_element_by_id("submit_store").click()
#         # Delete the store
#         selenium.find_element_by_xpath(
#             ".//*[@id='table_store']/tbody/tr[5]/td[4]/a").click()
#         time.sleep(3)
#         selenium.find_element_by_id("dashboard_store").click()
#         time.sleep(3)
#         selenium.quit()
