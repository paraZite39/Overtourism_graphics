import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

rasp_dataframe = pd.read_excel(r'C:\Users\User\Desktop\Supraturismul în Cluj-Napoca (răspunsuri).xlsx')

fig, ax = plt.subplots(figsize=(7.3,7))
fig.suptitle("Οcupație")

g = sns.countplot(y=rasp_dataframe["Ocupatie"], hue=rasp_dataframe["Sex"], palette=["lightpink","lightblue"], order=rasp_dataframe["Ocupatie"].value_counts().index)
g.set(xlabel=None, ylabel=None)
g.set_xticklabels(g.get_xticklabels(), rotation=0)

for p in g.patches:
    width = p.get_width()
    g.text(x = width + 0.35, y=p.get_y()+0.35, s = '{:.1f}%'.format(width / 143 * 100))
    
  