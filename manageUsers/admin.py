from django.contrib import admin

from .models import Customer,Manager,Employee


admin.site.register(Customer)
admin.site.register(Manager)
admin.site.register(Employee)

