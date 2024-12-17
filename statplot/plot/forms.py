from django import forms
from django.forms import formset_factory

class DataInputForm(forms.Form):
    csv_file = forms.FileField() #read csv file 

class VariablesForm(forms.Form):
    x = forms.CharField(max_length=100) #expected input is string
    y = forms.CharField(max_length=100) #expected input is string
    best_fit = forms.BooleanField(required=False)
    exponent = forms.IntegerField() 
    style= forms.ChoiceField(choices=[('darkgrid', 'darkgrid'), ('whitegrid', 'whitegrid'), ('dark', 'dark'), ('white', 'white'), ('ticks', 'ticks')]) #style of the plot
    Dx = forms.IntegerField(required=False) #for differentiation
    x1 = forms.IntegerField(required=False) #for integration 
    x2 = forms.IntegerField(required=False) #for integration
    regressionType = forms.ChoiceField(choices=[('polynomial', 'polynomial'), ('sin', 'sin'), ('logistic', 'logistic'), ('exponential', 'exponential')]) #type of regression
    


