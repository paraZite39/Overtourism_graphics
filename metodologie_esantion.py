import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set()
sns.set_style("darkgrid")
sns.set_palette("pastel")

rasp_dataframe = pd.read_excel(r'Supraturismul în Cluj-Napoca (răspunsuri).xlsx')

fig, ax = plt.subplots(3, 2, figsize=(8,8))
fig.suptitle("Profilul respondenților")
fig.tight_layout(h_pad=4, w_pad=2)

#SEXUL RESPONDENTILOR
labels_sex = "Βărbat", "Femeie"
counts_sex = [len(rasp_dataframe[rasp_dataframe["Sex"] == "Bărbat"]), len(rasp_dataframe[rasp_dataframe["Sex"] == "Femeie"])]

ax[0,0].pie(counts_sex, labels=labels_sex, autopct='%1.1f%%', colors=["lightblue", "lightpink"])
ax[0,0].title.set_text("Sexul respondenților")

#VARSTA RESPONDENTILOR (INDIFERENT DE SEX)
varsta = sns.histplot(rasp_dataframe["Varsta"], ax=ax[0,1], kde=True, bins=10)
ax[0,1].title.set_text("Vârsta respondenților")
varsta.set(xlabel=None, ylabel=None)

#VARSTA RESPONDENTILOR IN FUNCTIE DE SEX
sns.boxplot(x=rasp_dataframe["Varsta"], y=rasp_dataframe["Sex"], ax=ax[1,0], palette=["lightpink", "lightblue"], width=.5)
#sns.swarmplot(x=rasp_dataframe["Varsta"], y=rasp_dataframe["Sex"], ax=ax[0,1], color="gray", alpha=0.5) 
varsta_sex = sns.stripplot(data=rasp_dataframe, x="Varsta", y="Sex", ax=ax[1,0], color="gray", alpha=0.5)
ax[1,0].title.set_text("Vârsta respondenților (în funcție de sex)")
varsta_sex.set(xlabel=None, ylabel=None)


#NIVEL DE STUDII
g = sns.countplot(x=rasp_dataframe["Studii"], ax=ax[1,1], order=rasp_dataframe["Studii"].value_counts().index)
g.set_xticklabels(["Licență", "Liceu", "Masterat", "Doctorat", "Gimnaziu"], rotation=30)
g.set(xlabel=None, ylabel=None)
ax[1,1].title.set_text("Nivelul de studii")

for p in g.patches:
    height = p.get_height()
    g.text(x = p.get_x()+(p.get_width() / 2), y=height + 1.5, s = '{:.1f}%'.format(height / 143 * 100), ha = 'center')

#NiVEL DE VENITURI
labels_venit = "Sub 1500 RON;", "1500-3500 RON;", "Peste 3500 RON."
counts_venit = []
for label in labels_venit:
    counts_venit.append(len(rasp_dataframe[rasp_dataframe["Venit"] == label]))
    
ax[2,0].pie(counts_venit, labels=labels_venit, autopct='%1.1f%%')
ax[2,0].title.set_text("Venitul respondenților")

#group = rasp_dataframe["Ocupatie"].value_counts()
#sns.histplot(rasp_dataframe["Ocupatie"], ax=ax[2,0])

ax[2,1].title.set_text("Ani locuiți în Cluj-Napoca")
ani = sns.histplot(rasp_dataframe["Ani locuiti"], kde=True, ax=ax[2,1], bins=18)
ani.set(xlabel=None, ylabel=None)
