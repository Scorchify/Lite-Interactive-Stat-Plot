import matplotlib.pyplot as plot # type: ignore
import seaborn as sns # type: ignore
import seaborn.objects as so # type: ignore
import pandas # type: ignore

file = pandas.read_csv("data_histogram.csv")

#line overlay
#sns.displot(data=file, x="flipper_length_mm", kind="kde", bw_adjust=2)

p = so.Plot(file,"flipper_length_mm")
p2 = p.add(so.Bars(alpha=.3), so.Hist("density")).add(so.Line(), so.KDE())
p2.show()

plot.show()