from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('', views.view_item, name='iteminfo'),

    path('add_to_cart/',views.add_to_cart, name='add_to_cart'),
    path('view_cart', views.view_cart, name='view_cart'),
    path('create_order', views.create_order, name='create_order'),
    path('remove_from_cart/',views.remove_from_cart,name='remove_from_cart'),
    path('view_orders/',views.view_user_orders, name='view_user_orders'),
    path('remove_from_order/',views.remove_from_order,name='remove_from_order'),


]