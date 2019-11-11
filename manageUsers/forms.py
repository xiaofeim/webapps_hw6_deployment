from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=50)
    password = forms.CharField(
        label="Password", 
        max_length=12,
        widget = forms.widgets.PasswordInput(attrs={'type':'password'}),
    )

class RegisterForm(forms.Form):
    username = forms.CharField(
        label="User Name", 
        max_length=50, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        label="First Name",
        max_length=20, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=20, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Password", 
        max_length=12, 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )    
