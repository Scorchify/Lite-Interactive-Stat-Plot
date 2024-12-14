from django.urls import path, include
from . import views
from django.contrib import admin

app_name = 'plot'
urlpatterns = [
#home page 
path('', views.index, name='index'),
#graphing page 
path('plot/',views.graph, name='plot'),
#data view
path('data/', views.data_view, name='data_view'),

]