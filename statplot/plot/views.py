from django.shortcuts import render
import csv
import sys
from django.http import HttpResponse
from io import TextIOWrapper
from .forms import DataInputForm
from plot.stat_calc import print_vals, set_vals

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
matplotlib.use('Agg')
from io import BytesIO
import base64
import os
from django.conf import settings

# Variables
x = "velocity"
y = "time"
exponent = 1
regressionType = "polynomial"
path_to_csv = ""
best_fit = True
stats = None

# Create your views here.
def index(request):
    return render(request, 'index.html')

def graph(request):
    global path_to_csv, x, y, exponent, regressionType, best_fit, stats # Declare the variable as global to modify it
    if request.method == 'POST':
        form = DataInputForm(request.POST, request.FILES)
        if form.is_valid():
            x = request.POST.get('x')
            y = request.POST.get('y')
            regressionType = request.POST.get('regressionType')
            exponent = int(request.POST.get('exponent'))
            best_fit = True

            csv_file = request.FILES.get('csv_file')
            if csv_file:
                try:
                    temp_file_path = os.path.join(settings.MEDIA_ROOT, csv_file.name)
                    with open(temp_file_path, 'wb+') as destination:
                        for chunk in csv_file.chunks():
                            destination.write(chunk)

                    path_to_csv = temp_file_path

                    # Read the CSV file
                    data = pd.read_csv(temp_file_path)
                    set_vals(path_to_csv, x, y)
                    stats = print_vals(regressionType, exponent)
                except pd.errors.ParserError:
                    form.add_error('csv_file', 'The CSV file is formatted incorrectly.')
                    return render(request, 'plot.html', {'form': form})
                
                plt.figure(figsize=(10, 6))
                if best_fit:
                    sns.lmplot(x=x, y=y, data=data, ci=None, scatter_kws={"s": 80}, order=exponent)
                else:
                    sns.scatterplot(data=data, x=x, y=y)
                buffer = BytesIO()
                plt.savefig(buffer, format='png')
                buffer.seek(0)
                image_png = buffer.getvalue()
                buffer.close()
                image_base64 = base64.b64encode(image_png).decode('utf-8')
                return render(request, 'plot.html', {'form': form, 'graph': image_base64})
            else:
                form.add_error('csv_file', 'Required Field.')
            

    else:
        form = DataInputForm()
    return render(request, 'plot.html', {'form': form})