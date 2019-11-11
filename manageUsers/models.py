from django.db import models
from manageStores.models import Restaurant
from django.contrib.auth.models import User


class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    c_name = models.CharField(max_length=50)

    def __str__(self):
        return self.c_name


class Employee(models.Model):
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    e_name = models.CharField(max_length=50)
    restaurant = models.ManyToManyField(Restaurant)

    def __str__(self):
        return self.e_name


class Manager(models.Model):
    manager = models.OneToOneField(User, on_delete=models.CASCADE)
    m_name = models.CharField(max_length=50)
    restaurant = models.ManyToManyField(Restaurant)

    def __str__(self):
        return self.m_name
