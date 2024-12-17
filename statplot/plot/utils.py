from django.http import HttpResponse
from django.shortcuts import render
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import base64
import statistics as st
import numpy as np 
from sympy import symbols, diff, integrate
from scipy.optimize import curve_fit
import scipy.stats as scipy

matplotlib.use('Agg')

#user inputted variables
x = "velocity"
y = "time"
exponent = 2
regressionType = "polynomial"
path_to_csv = ""
best_fit = True
theme = "whitegrid"
x1 = 0
x2 = 10

#range function 
def getRange(data):
    minimum = min(data)
    maximum = max(data)
    return maximum-minimum

#sine function
def sineFunction(x, A, B, C, D):
    return A * np.sin(B * x + C) + D #form of a sine function

#pearson correlation coeffecient (returns [-1,1])
def pearsonFunc(x,y):
    pearsons_correlation_coefficient = scipy.pearsonr(x, y)
    pearson = pearsons_correlation_coefficient[0]
    return pearson

def regressionEquation(x,y):
    if(regressionType=="polynomial"):
        coefficients = np.polyfit(data_x, data_y, exponent)
        slope = coefficients[0]
        intercept = coefficients[1]
        return slope*x**exponent+intercept #return the poly regression 
    
    elif regressionType=="sin":
        initial_guess = [2, 1.5, 0, 0]
        params, covariance = curve_fit(sine_function, data_x, data_y, p0=initial_guess)
        A_fit, B_fit, C_fit, D_fit = params
        return A_fit*sin(B_fit*x-C_fit)+D_fit
    
    else:
        return 1
    
    def assignDataVar(data):
        data = pd.read_csv("data_scatter.csv")
        data_x = data[x]
        data_y = data[y]

        symbolx, symboly = symbols('x y')
        expr = regressionEquation(symbolx,symboly)
        
        expr_diff = diff(expr, symbolx) #derivative of the regression equation at symbolx
        expr_diff2 = diff(expr_diff, symbolx) #second derivative of the regression equation at symbolx 
        
        expr_integral = integrate(expr, (symbolx, min(data_x), max(data_x))) #integrates the function over desired interval TODO Change to user input 
        #usable vars 
        derivative = expr_diff.doit() #evaluate the derivative at symbolx 
        derivative2 = expr_diff2.doit() #evaluate the second derivative at symbolx 
        integral = expr_integral.doit()


        #output variables 
        mean_x = st.mean(data_x)
        mean_y = st.mean(data_y)
        range_x = getRange(data_x)
        range_y = getRange(data_y)
        std_dev_x = st.stdev(data_x)
        std_dev_y = st.stdev(data_y)
        pearson = pearsonFunc(data_x, data_y)
        x_variance = st.variance(data_x)
        y_variance = st.variance(data_y)
        x_median = st.median(data_x)
        y_median = st.median(data_y)
        x_mode = st.mode(data_x)
        y_mode = st.mode(data_y)
        x_skew = st.stdev(data_x)
        y_skew = st.stdev(data_y)




        
