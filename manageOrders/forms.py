from django import forms
from django.forms import ModelForm
from addtocart.models import Cart, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['cart','total_price','modify_date' ]
        error_messages = {
            'customer':{'required':"Customer Name should not be empty",},
            'modify_date':{'required':"Modified Date should not be early than now",},
        }