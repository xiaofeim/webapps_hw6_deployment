from django import forms
from .models import GlobalMenu, Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
