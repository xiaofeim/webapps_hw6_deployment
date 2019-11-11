from django.contrib import admin
from django.urls import path
from manageItems import views

urlpatterns = [
    path('', views.view_all_items, name='menuinfo'),
    # Create a new menu item
    path('add/',views.add_iteminfo,name='add_iteminfo'),
    path('edit/',views.edit_iteminfo,name='edit_iteminfo'),
    path('delete/',views.delete_iteminfo,name='delete_iteminfo'),

]