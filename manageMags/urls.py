from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_all_managers, name='managerinfo'),
    path('add/',views.add_manager,name='add_manager'),
    path('edit/',views.add_store_manager,name='add_store_manager'),
    path('delete/',views.delete_manager,name='delete_manager'),
    path('remove_store_manager/',views.remove_store_manager,name='remove_store_manager'),

]