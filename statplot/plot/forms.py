from django import forms
from django.forms import formset_factory

class DataInputForm(forms.Form):
    csv_file = forms.FileField()

    

