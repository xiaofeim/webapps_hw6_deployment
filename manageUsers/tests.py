# from django.test import TestCase,LiveServerTestCase
# from selenium import webdriver
# from django.contrib.auth.models import User
# from .models import Customer,Employee,Manager
# from django.test import TestCase
# from manageStores.models import Restaurant

# class testCustomer(TestCase):
#     def test_customer(self):
#         user = User.objects.create_user(
#                     username="UTCustomer",
#                     first_name="UT",
#                     last_name="Customer",
#                     password="UTCustomer"
#                 )
#         customer = Customer.objects.create(customer=user,c_name="UTCustomer")
#         self.assertEqual("UTCustomer",customer.c_name)     

# class testEmployee(TestCase):
#     def test_employee(self):
#         user = User.objects.create_user(
#                     username="UTEmployee",
#                     first_name="UT",
#                     last_name="Employee",
#                     password="UTEmployee"
#                 )
#         employee = Employee.objects.create(employee=user,e_name="UTEmployee")
#         self.assertEqual("UTEmployee",employee.e_name)     

# class testManager(TestCase):
#     def test_manager(self):
#         user = User.objects.create_user(
#                     username="UTManager",
#                     first_name="UT",
#                     last_name="Manager",
#                     password="UTManager"
#                 )
#         manager = Manager.objects.create(manager=user,m_name="UTManager")
#         self.assertEqual("UTManager",manager.m_name)     


# class UserTestCase(LiveServerTestCase):
#     def setUp(self):
#         self.selenium = webdriver.Chrome()
#         super(UserTestCase, self).setUp()
#     def test_user(self):
#         selenium = self.selenium
#         selenium.get('http://127.0.0.1:8000/')
#         # Test register function
#         selenium.find_element_by_id("register").click()
#         selenium.find_element_by_id("id_username").send_keys("seleniumTest")
#         selenium.find_element_by_id("id_first_name").send_keys("selenium")
#         selenium.find_element_by_id("id_last_name").send_keys("Test")
#         selenium.find_element_by_id("id_password").send_keys("seleniumTest")
#         selenium.find_element_by_id("register_submit").click()
#         # Test log out function
#         selenium.find_element_by_id("logout").click()
#         # Test log in function
#         selenium.find_element_by_id("login").click()
#         selenium.find_element_by_id("id_username").send_keys("seleniumTest")
#         selenium.find_element_by_id("id_password").send_keys("seleniumTest")
#         selenium.find_element_by_id("login_submit").click()