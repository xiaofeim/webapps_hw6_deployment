from django import forms
from manageStores.models import Restaurant
from manageUsers.models import Employee


class EmployeeForm(forms.Form):
    e_name = forms.CharField(label="Employee Name", max_length=50)
    restaurant = forms.MultipleChoiceField(
            choices= Restaurant.objects.all().values_list('id','restauran_location'),
            label = "Restaurant Location",
            initial = ['1'],
            widget = forms.widgets.CheckboxSelectMultiple(),
    )

class ERelationForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'