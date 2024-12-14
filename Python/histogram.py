import matplotlib.pyplot as plot # type: ignore
import seaborn as sns # type: ignore
import seaborn.objects as so # type: ignore
import pandas # type: ignore
from values import path_to_csv, x

def make_hisogram(path_to_csv, x):
    file = pandas.read_csv(path_to_csv)
    #line overlay
    #sns.displot(data=file, x="flipper_length_mm", kind="kde", bw_adjust=2)

    p = so.Plot(file,x)
    p2 = p.add(so.Bars(alpha=.3), so.Hist("density")).add(so.Line(), so.KDE())
    p2.show()

    plot.show()
