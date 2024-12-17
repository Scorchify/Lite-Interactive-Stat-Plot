from django.shortcuts import render
import csv
from django.http import HttpResponse
from io import TextIOWrapper
from .forms import DataInputForm, VariablesForm
import plotly.express as px 
import plotly.graph_objects as go
import numpy as np
import pandas as pd

import os
from django.conf import settings

# Variables
x = "velocity"
y = "time"
exponent = 1
regressionType = "polynomial"
path_to_csv = ""
best_fit = True

# Create your views here.
def index(request):
    return render(request, 'index.html')

def plotly(request): 
    global path_to_csv
    if request.method == 'POST':
        form = DataInputForm(request.POST, request.FILES)
        if form.is_valid(): 
            csv_file = request.FILES.get('csv_file') # gets csv file from form
            df = pd.read_csv(csv_file) # reads csv file

            fig = px.scatter(df, x="velocity", y="time", title="Velocity vs Time") # creates scatter plot
            graph_html = fig.to_html(full_html=False) # converts plot to HTML
            return render(request, 'plot.html', {'form': form, 'graph_html': graph_html}) # returns plot.html with the plot
        else: 
            return render(request, 'plot.html', {'form': form}) # returns plot.html with the form
    else: 
        form = DataInputForm()
        return render(request, 'plot.html', {'form': form}) # returns plot.html with the form
    

# def graph(request):
#     global path_to_csv 
#     if request.method == 'POST':
#         form = DataInputForm(request.POST, request.FILES)
#         variables_form = VariablesForm(request.POST)
#         if form.is_valid() and variables_form.is_valid():
#             csv_file = request.FILES.get('csv_file')
#             if csv_file:
#                 try:
#                     temp_file_path = os.path.join(settings.MEDIA_ROOT, csv_file.name)
#                     with open(temp_file_path, 'wb+') as destination:
#                         for chunk in csv_file.chunks():
#                             destination.write(chunk)

#                     path_to_csv = temp_file_path

#                     # Read the CSV file
#                     df = pd.read_csv(temp_file_path)
#                     data = df.to_dict(orient='records')
#                     print("CSV file read successfully")
                
#                     # Get vars
#                     x = variables_form.cleaned_data['x']
#                     y = variables_form.cleaned_data['y']
#                     best_fit = variables_form.cleaned_data['best_fit']
#                     style = variables_form.cleaned_data['style']
#                     Dx = variables_form.cleaned_data['Dx']
#                     x1 = variables_form.cleaned_data['x1']
#                     x2 = variables_form.cleaned_data['x2']
#                     regressionType = variables_form.cleaned_data['regressionType']
#                     exponent = variables_form.cleaned_data['exponent']
#                     title = variables_form.cleaned_data['title']

#                     # Generate scatter plot with regression line if regressionType != None
#                     fig = px.scatter(df, x=x, y=y, title=title)
#                     if best_fit:
#                         if regressionType == 'polynomial':
#                             coefficients = np.polyfit(df[x], df[y], exponent)
#                             poly = np.poly1d(coefficients)
#                             df['fit'] = poly(df[x])
#                             fig.add_scatter(x=df[x], y=df['fit'], mode='lines', name='Fit Line')

#                     # Convert the figure to HTML
#                     graph_html = fig.to_html(full_html=False)

#                     return render(request, 'plot.html', {
#                         'form': form,
#                         'variables_form': variables_form,
#                         'graph_html': graph_html
#                     })

#                 except pd.errors.ParserError:
#                     form.add_error('csv_file', 'The CSV file is formatted incorrectly.')
#                     return render(request, 'plot.html', {'form': form, 'variables_form': variables_form})
#             else:
#                 form.add_error('csv_file', 'Please upload a CSV file or manually enter data to get started.')
#                 return render(request, 'plot.html', {'form': form, 'variables_form': variables_form})
#         else: 
#             print("Form is not valid")
#             return render(request, 'plot.html', {'form': form, 'variables_form': variables_form})
#     else: 
#         form = DataInputForm()
#         variables_form = VariablesForm()
#         return render(request, 'plot.html', {'form': form, 'variables_form': variables_form})