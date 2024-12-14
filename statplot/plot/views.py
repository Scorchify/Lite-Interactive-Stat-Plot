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



# Create your views here.
def index(request):
    return render(request, 'index.html')

def graph(request):
    if request.method == 'POST':
        form = DataInputForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES.get('csv_file')
            if csv_file:
                try:
                    data = pd.read_csv(csv_file)
                except pd.errors.ParserError:
                    form.add_error('csv_file', 'The CSV file is formatted incorrectly.')
                    return render(request, 'plot.html', {'form': form})
                
                plt.figure(figsize=(10, 6))
                sns.regplot(data=data, x='x', y='y')
                buffer = BytesIO()
                plt.savefig(buffer, format='png')
                buffer.seek(0)
                image_png = buffer.getvalue()
                buffer.close()
                image_base64 = base64.b64encode(image_png).decode('utf-8')
                return render(request, 'plot.html', {'form': form, 'graph': image_base64})
            else:
                form.add_error('csv_file', 'This field is required.')
    else:
        form = DataInputForm()
    return render(request, 'plot.html', {'form': form})

