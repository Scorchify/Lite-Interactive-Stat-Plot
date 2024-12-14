from django import forms
from django.forms import formset_factory

class DataInputForm(forms.Form):
    x = forms.CharField(label='X', max_length=100)
    y = forms.CharField(label='Y', max_length=100)
    color = forms.CharField(label='Color', max_length=100)
    point_type = forms.CharField(label='Point Type', max_length=100)
    group = forms.CharField(label='Group', max_length=100, required=False)
    
DataInputFormSet = formset_factory(DataInputForm, extra=1)

class InputOther(forms.Form):
    #domain restriction
    x1 = forms.FloatField(label='X1')
    x2 = forms.FloatField(label='X2')

    #range restriction
    y1 = forms.FloatField(label='Y1')
    y2 = forms.FloatField(label='Y2')
    
