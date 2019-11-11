from django import forms
from addtocart.models import Cart

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['item_qty']
