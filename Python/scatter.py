# Import seaborn
import matplotlib.pyplot as p
import seaborn as sns
import seaborn.objects as so
import pandas
import numpy as np

sns.set_theme()
file = pandas.read_csv("data_scatter.csv")

# plot = so.Plot(
#     data=file,
#     x="x", y="y"
# ).add(so.Dot()).add(so.Line(), so.PolyFit())

sns.regplot(file, x="x", y="y")

p.show()
