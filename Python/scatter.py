# Import seaborn
import matplotlib.pyplot as p
import seaborn as sns
import seaborn.objects as so
import pandas
import numpy as np
from values import path_to_csv, best_fit, x, y, exponent

def make_scatter():
    sns.set_theme()
    file = pandas.read_csv(path_to_csv)

    # plot = so.Plot(
    #     data=file,
    #     x="x", y="y"
    # ).add(so.Dot()).add(so.Line(), so.PolyFit())

    if best_fit:
        sns.regplot(file, x=x, y=y)
    else:
        sns.scatterplot(file, x=x, y=y, order=exponent)

    p.show()
