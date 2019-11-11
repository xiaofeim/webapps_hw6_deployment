from django import forms
from manageStores.models import Restaurant
from manageUsers.models import Manager


class ManagerForm(forms.Form):
    m_name = forms.CharField(label="Manager Name", max_length=50)
    restaurant = forms.MultipleChoiceField(
            choices= Restaurant.objects.all().values_list('id','restauran_location'),
            label = "Restaurant Location",
            initial = ['1'],
            widget = forms.widgets.CheckboxSelectMultiple(),
    )

class MRelationForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'