import pandas
import math
import statistics as st
import numpy as np # type: ignore
from values import x,y,exponent,regressionType
from sympy import *
from scipy.optimize import curve_fit
import scipy.stats as scipy

# this comment is my biggest contribution
# :)
def getrange(data):
    minimum = min(data)
    maximum = max(data)
    return maximum-minimum

def sine_function(x, A, B, C, D):
    return A * np.sin(B * x + C) + D

# (data[x], data[y])
def pearsonfunc(x, y):
    pearsons_correlation_coefficient = scipy.pearsonr(x, y)
    pearson = pearsons_correlation_coefficient[0]
    return pearson

def regressionEquation(x,y):
    if(regressionType=="polynomial"):
        
        coefficients = np.polyfit(thisx, thisy, exponent)
        slope = coefficients[0]
        intercept = coefficients[1]
        return slope*x**exponent+intercept
        
    elif regressionType=="sin":
        initial_guess = [2, 1.5, 0, 0]
        params, covariance = curve_fit(sine_function, thisx, thisy, p0=initial_guess)
        A_fit, B_fit, C_fit, D_fit = params
        return A_fit*sin(B_fit*x-C_fit)+D_fit

    else:
        return 1
data,y_mean,y_median,y_mode,y_vals,y_variance,y_range,thisx,thisy=None

def set_vals(path_to_csv):
    global data,y_mean,y_median,y_mode,y_vals,y_variance,y_range,thisy,thisx

    data = pandas.read_csv(path_to_csv)

    # Basic statistics
    # range is local func
    y_vals = data[y].tolist()
    x_vals = data[x].tolist()
    y_mean = st.mean(y_vals)
    y_median = st.median(y_vals)
    y_mode = st.mode(y_vals)
    y_variance = st.variance(y_vals)
    y_range = getrange(y_vals)


    # find equation of regression
    thisy = data[y]
    thisx = data[x]


# print("Equation: y = {:.2f}x + {:.2f}".format(slope, intercept))

def print_vals():
    #setup
    symbolx, symboly = symbols('x y')
    expr = regressionEquation(symbolx,symboly)

    # regression options

    print("Expression : {}".format(expr))
    

    # derivative of regression equation
    expr_diff = Derivative(expr, x)  
    # integral of regression equation
    expr_integ = integrate(expr, (x,min(x_vals),max(x_vals)))
        
    print("Derivative of expression with respect to x : {}".format(expr_diff))  
    #pearson
    pearsons_correlation_coefficient = scipy.pearsonr(x, y)
    return "Value of the derivative : {}".format(expr_diff.doit()),"Value of the integral : {}".format(expr_integ.doit()), pearsons_correlation_coefficient[0]



