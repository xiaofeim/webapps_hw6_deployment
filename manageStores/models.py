from django.db import models
from manageItems.models import GlobalMenu


class Restaurant(models.Model):
    global_menu = models.ForeignKey(GlobalMenu, on_delete=models.PROTECT)
    restauran_location = models.CharField(max_length=20)
    def __str__(self):
        return self.restauran_location
