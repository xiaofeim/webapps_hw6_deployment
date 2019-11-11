import datetime
from django.db import models
from django.utils import timezone
from manageItems.models import GlobalMenu, Item
from manageUsers.models import Customer
from manageStores.models import Restaurant

from django.contrib.auth.models import User

class Cart(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_qty = models.PositiveIntegerField(default=1)
    submitted_status = models.CharField(max_length=100)
    modify_date = models.DateTimeField('modify date',default = timezone.now)


class Order(models.Model):
    status_choice = (
        ('Urgent','Urgent'),
        ('Invalid','Invalid'),
        ('Awaitting Processing','Awaitting Processing'),
        ('Transfer To Kitchen','Transfer To Kitchen'),
        ('Ready For Shipping','Ready For Shipping'),
        ('Delivered','Delivered')
    )
    cart = models.ManyToManyField(Cart)
    total_price = models.IntegerField(default=0)
    # user field represents the current log-in customer's username.
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # restaurant = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    # customer_name field represents the name customer entered when places an order.
    # It can be different from username.
    customer_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100,choices= status_choice,default = 'Awaitting Processing')
    modify_date = models.DateTimeField('modify date',default = timezone.now)
