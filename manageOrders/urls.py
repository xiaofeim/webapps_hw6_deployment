from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_orders, name='orderinfo'),
    path('edit_submitted_orders', views.edit_submitted_orders, name='edit_submitted_orders'),
    path('delete_submitted_orders',views.delete_submitted_orders,name='delete_submitted_orders'),

]