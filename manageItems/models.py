import datetime
from django.db import models
from django.utils import timezone

class GlobalMenu(models.Model):
    global_menu_name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')    
    def __str__(self):
        return self.global_menu_name

class Item(models.Model):
    global_menu = models.ForeignKey(GlobalMenu, on_delete=models.PROTECT)
    item_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=200)
    item_price = models.PositiveIntegerField(default=0)
    item_img = models.FileField(upload_to='img',null=True)
    def __str__(self):
        return self.item_name


