from django.shortcuts import render
import csv
from django.http import HttpResponse
from io import TextIOWrapper
from .forms import DataInputFormSet

# Create your views here.
def index(request):
    return render(request, 'index.html')

def graph(request):
    return render(request, 'plot.html') 

def data_view(request):
    if request.method == "POST" and 'csv_file' in request.FILES:
        csv_file = request.FILES['csv_file']

        # Ensure it's a valid CSV file
        if not csv_file.name.endswith('.csv'):
            return render(request, 'plot.html', {
                'error': 'Please upload a valid CSV file.',
            })

        try:
            # Read the uploaded CSV file
            data = TextIOWrapper(csv_file.file, encoding='utf-8')
            reader = csv.DictReader(data)
            
            # Verify the required columns
            required_columns = {'x', 'y', 'color', 'point_type', 'group'}
            if not required_columns.issubset(reader.fieldnames):
                return render(request, 'plot.html', {
                    'error': 'CSV file must contain columns: x, y, color, point_type, group.',
                })

            # Collect the data to display in the table
            csv_data = [row for row in reader]

            return render(request, 'plot.html', {
                'csv_data': csv_data,
                'columns': required_columns,
            })

        except Exception as e:
            return render(request, 'plot.html', {
                'error': f'Error processing CSV file: {str(e)}',
            })

    # Render the upload page if not POST
    return render(request, 'plot.html')