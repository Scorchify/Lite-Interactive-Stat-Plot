import pandas
import statistics as st
import numpy as np # type: ignore
from values import x,y,regression
from sympy import *
def getrange(data):
    minimum = min(data)
    maximum = max(data)
    return maximum-minimum

data = pandas.read_csv("data_scatter.csv")

# basic stuff, cool
y_vals = data[y].tolist()
y_mean = st.mean(y_vals)
y_median = st.median(y_vals)
y_mode = st.mode(y_vals)
y_variance = st.variance(y_vals)
y_range = getrange(y_vals)


thisy = data[y]
thisx = data[x]
coefficients = np.polyfit(thisx, thisy, regression)  # 1 for linear regression
slope = coefficients[0]
intercept = coefficients[1]
exponent = regression

print("Equation: y = {:.2f}x + {:.2f}".format(slope, intercept))

x, y = symbols('x y')
expr = slope*x**exponent+intercept
print("Expression : {}".format(expr))
  
# Use sympy.Derivative() method 
expr_diff = Derivative(expr, x)  
expr_integ = integrate(expr, (x,min(y_vals),max(y_vals)))
     
print("Derivative of expression with respect to x : {}".format(expr_diff))  
print("Value of the derivative : {}".format(expr_diff.doit()))
print("Value of the integral : {}".format(expr_integ.doit()))


# pearsons correlation coefficient
