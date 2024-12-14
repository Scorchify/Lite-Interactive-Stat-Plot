from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def graph(request):
    return render(request, 'plot.html')
