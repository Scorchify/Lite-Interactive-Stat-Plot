from django.urls import path, include
from . import views
from django.contrib import admin

app_name = 'plot'
urlpatterns = [
#home page 
path('', views.index, name='index'),
#graphing page 
path('plot/',views.plotly, name='plot'),
#data view


]