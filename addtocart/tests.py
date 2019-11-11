# from django.test import TestCase, LiveServerTestCase
# from selenium import webdriver
# from django.contrib.auth.models import User
# import time
# from manageItems.models import GlobalMenu, Item
# from .models import Cart, Order
# from manageStores.models import Restaurant
# from manageUsers.models import Customer
# from django.utils import timezone


# class testCart(TestCase):
#     def test_cart(self):
#         global_menu = GlobalMenu.objects.create(
#             global_menu_name="TestMenu", pub_date=timezone.now())
#         item = Item.objects.create(global_menu=global_menu, item_name="UTItem",
#                                    item_description="Test Description", item_price=100)
#         modify_date = timezone.now()
#         cart = Cart.objects.create(
#             item=item, item_qty=100, submitted_status="Awaiting Processing", modify_date=modify_date)
#         self.assertEqual(100, cart.item_qty)
#         self.assertEqual("Awaiting Processing", cart.submitted_status)
#         self.assertEqual("UTItem", cart.item.item_name)


# class testOrder(TestCase):
#     def test_order(self):
#         status = "Urgent"
#         global_menu = GlobalMenu.objects.create(
#             global_menu_name="TestMenu", pub_date=timezone.now())
#         item = Item.objects.create(global_menu=global_menu, item_name="UTItem",
#                                    item_description="Test Description", item_price=100)
#         cart1 = Cart.objects.create(
#             item=item, item_qty=100, submitted_status="Awaiting Processing", modify_date=timezone.now())
#         total_price = 1000
#         user = User.objects.create_user(
#             username="UTOrder",
#             first_name="UT",
#             last_name="Order",
#             password="UTOrder"
#         )
#         customer = Customer.objects.create(customer=user, c_name="UTOrder")
#         restaurant = Restaurant.objects.create(
#             global_menu=global_menu, restauran_location="TestRestaurant")
#         customer_name = "TestCustomerName"
#         order = Order.objects.create(
#             total_price=total_price,
#             user=customer,
#             restaurant=restaurant,
#             customer_name=customer_name,
#             status=status,
#             modify_date=timezone.now()
#         )
#         order.cart.add(cart1.id)
#         self.assertEqual(1000, order.total_price)
#         self.assertEqual("Urgent", order.status)
#         self.assertEqual("TestRestaurant", order.restaurant.restauran_location)
#         self.assertEqual("TestCustomerName", order.customer_name)

# class placeAnOrderTestCase(LiveServerTestCase):
#     def setUp(self):
#         self.selenium = webdriver.Chrome()
#         super(placeAnOrderTestCase, self).setUp()
#     def test_register(self):
#         selenium = self.selenium
#         selenium.get('http://127.0.0.1:8000/')
#         selenium.find_element_by_id("login").click()
#         selenium.find_element_by_id("id_username").send_keys("seleniumTest")
#         selenium.find_element_by_id("id_password").send_keys("seleniumTest")
#         selenium.find_element_by_id("login_submit").click()
#         selenium.find_element_by_id("placeAnOrder").click()
#         selenium.find_element_by_id("cart_button_5").click()
#         selenium.find_element_by_id("cart_button_4").click()
#         time.sleep(5)
#         selenium.find_element_by_id("view_cart").click()
#         time.sleep(5)
#         # Test place an order function
#         selenium.find_element_by_id("btn_place_order").click()
#         time.sleep(3)
#         selenium.find_element_by_id("order_name").send_keys("seleniumTest")
#         selenium.find_element_by_id("submit_order").click()
#         time.sleep(3)
#         selenium.find_element_by_id("view_orders").click()
#         selenium.find_element_by_id("dashboard").click()
#         time.sleep(3)
#         # Close the driver
#         selenium.quit()
