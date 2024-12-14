from django.shortcuts import render
import csv
from django.http import HttpResponse
from io import TextIOWrapper
from .forms import DataInputForm

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

# Create your views here.
def index(request):
    return render(request, 'index.html')

def graph(request):
    global path_to_csv  # Declare the variable as global to modify it
    if request.method == 'POST':
        form = DataInputForm(request.POST, request.FILES)
        if form.is_valid():
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
                except pd.errors.ParserError:
                    form.add_error('csv_file', 'The CSV file is formatted incorrectly.')
                    return render(request, 'plot.html', {'form': form})
                
                plt.figure(figsize=(10, 6))
                if best_fit:
                    sns.regplot(data=data, x=x, y=y)
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