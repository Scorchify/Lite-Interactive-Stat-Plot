import matplotlib.pyplot as p
import seaborn as sns
import pandas as pd
import numpy as np
from io import BytesIO
import base64
from values import path_to_csv, best_fit, x, y, exponent

def make_scatter(path_to_csv, best_fit, x, y, exponent):
    sns.set_theme()
    file = pd.read_csv(path_to_csv)

    plt.figure(figsize=(10, 6))
    if best_fit:
        sns.regplot(data=file, x=x, y=y)
    else:
        sns.scatterplot(data=file, x=x, y=y, order=exponent)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    image_base64 = base64.b64encode(image_png).decode('utf-8')
    return image_base64