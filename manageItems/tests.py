from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from django.contrib.auth.models import User
from manageUsers.models import Manager
from selenium.webdriver.support.ui import Select
import time
from django.test import TestCase
from .models import GlobalMenu, Item
from django.utils import timezone


class testMenu(TestCase):
    def test_menu_name(self):
        global_menu = GlobalMenu.objects.create(
            global_menu_name="TestMenu", pub_date=timezone.now())
        self.assertEqual("TestMenu", global_menu.global_menu_name)


class testItem(TestCase):
    def test_item_name(self):
        global_menu = GlobalMenu.objects.create(
            global_menu_name="TestMenu", pub_date=timezone.now())
        item = Item.objects.create(global_menu=global_menu, item_name="UTItem",
                                   item_description="Test Description", item_price=100)
        self.assertEqual("UTItem", item.item_name)


class ItemTestCase(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()
        super(ItemTestCase, self).setUp()

    def test_manage_items(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/')
        # Log-in as the Manager role
        selenium.find_element_by_id("login").click()
        selenium.find_element_by_id("id_username").send_keys("MagSeleniumTest")
        selenium.find_element_by_id("id_password").send_keys("MagSeleniumTest")
        selenium.find_element_by_id("login_submit").click()
        # Test create, edit and delete menu item
        # Add a new item
        selenium.find_element_by_id("manageItems").click()
        # selenium.find_element_by_id("add_item").click()
        # select = Select(selenium.find_element_by_id("id_global_menu"))
        # select.select_by_visible_text("Menu")
        # selenium.find_element_by_id("id_item_name").send_keys("ItemSeleniumTest")
        # selenium.find_element_by_id("id_item_description").send_keys("ItemSeleniumTest")
        # selenium.find_element_by_id("id_item_price").send_keys("10")
        # selenium.find_element_by_id("id_item_img").click(r'/media/img/6.PNG')
        # selenium.find_element_by_id("btn_item").click()
        # time.sleep(3)
        # Edit the item
        selenium.find_element_by_xpath(
            ".//*[@id='item_table']/tbody/tr[1]/td[6]/a[@id='edit_iteminfo']").click()
        selenium.find_element_by_id("id_item_name").send_keys("SeleniumTest")
        selenium.find_element_by_id("submit_item").click()
        time.sleep(3)
        # Delete the item
        selenium.find_element_by_xpath(
            ".//*[@id='item_table']/tbody/tr[1]/td[6]/a[@id='delete_iteminfo']").click()
        selenium.find_element_by_id("dashboard_item").click()
        time.sleep(3)
        selenium.quit()
