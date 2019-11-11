from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_all_stores, name='storeinfo'),
    path('add/',views.add_store,name='add_store'),
    path('edit/',views.edit_store,name='edit_store'),
    path('delete/',views.delete_store,name='delete_store'),
]
