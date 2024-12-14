# Import seaborn
import matplotlib.pyplot as plot
import seaborn as sns
import pandas

# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = pandas.read_csv("data.csv")

# Create a visualization
sns.relplot(
    data=tips
)
plot.show()
