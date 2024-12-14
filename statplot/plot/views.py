from django.shortcuts import render
import csv
from django.http import HttpResponse
from .forms import DataInputFormSet

# Create your views here.
def index(request):
    return render(request, 'index.html')

def graph(request):
    return render(request, 'plot.html') 

def data_view(request):
    if request.method == "POST":
        formset = DataInputFormSet(request.POST)
        if formset.is_valid():
            data = formset.cleaned_data
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="data.csv"'
            writer = csv.writer(response)
            writer.writerow(['x', 'y', 'color', 'point_type', 'group'])
            
            for form in formset: 
                writer.writerow([
                    form.cleaned_data['x'],
                    form.cleaned_data['y'],
                    form.cleaned_data['color'],
                    form.cleaned_data['point_type'],
                    form.cleaned_data['group']
                ])
                return response
            else:
                formset = DataInputFormSet()
            return render(request, 'data.html', {'formset': formset})
