from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_all_employees, name='employeeinfo'),
    path('add/',views.add_employee,name='add_employee'),
    path('edit/',views.add_store_employee,name='edit_employee'),
    path('delete/',views.delete_employee,name='delete_employee'),
    path('remove_store_employee/',views.remove_store_employee,name='remove_store_employee'),

]