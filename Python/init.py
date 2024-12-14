# Import seaborn
import matplotlib.pyplot as plot
import seaborn as sns
import seaborn.objects as so
import pandas

sns.set_theme()
file = pandas.read_csv("data.csv")

so.Plot(
    data=file,
    x="x", y="y"
).add(so.Dot())

sns.lmplot(x="x", y="y", data=file)

plot.show()
