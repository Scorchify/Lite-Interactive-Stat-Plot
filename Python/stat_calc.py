import pandas
import statistics
from values import x,y
data = pandas.read_csv("data_scatter.csv")

y_vals = data[y].tolist()
y_mean = statistics.mean(y_vals)
y_median = statistics.median(y_vals)
y_mode = statistics.mode(y_vals)

data[y]