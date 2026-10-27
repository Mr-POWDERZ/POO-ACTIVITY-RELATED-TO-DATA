### Activite 8 :
    
#%% Etape 1 : :
    
import pandas as pd
df = pd.read_csv(r"C:\Users\dell\Downloads\qualite_industrielle.csv")
print(df)

#%% Q1 :
print(df.shape)

#%% Q2 :
print(df.head())
#%% Q3 :
print(df.columns)

#%% Q4 :
print(df.info())

#%% Q5 :
print(df.isnull().sum())

#%% Q6 :
print(df.duplicated().sum())

#%% Etape 2 :

#%%Q7 :
print(df.describe())

#%%Q8 :
print(df["Produit"].value_counts())

#%%Q9:
print(df["Ligne_Production"].value_counts())

#%% Etape 3 :
    
#%%Q10:
df = df.drop_duplicates()

#%%Q11:
df.to_csv("qualite_industrielle_nettoyee.csv", index=False)

#%% Graphiques : 

#%% Graphe 1 : Barres
import matplotlib.pyplot as plt
import numpy as np

taux = df.groupby("Produit")["Taux_Defauts_pct"].mean()

plt.figure(figsize=(7, 5))
bars = plt.bar(taux.index, taux.values, color=["#4C72B0", "#DD8452", "#55A868", "#C44E52"])
for b in bars:
    plt.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.1,
             f"{b.get_height():.2f} %", ha="center")
plt.title("Taux moyen de défauts par produit")
plt.xlabel("Produit")
plt.ylabel("Taux de défauts moyen (%)")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

#%% Graphique 2 : Nuage de points
plt.figure(figsize=(7, 5))
for res, couleur in [("Conforme", "green"), ("Non conforme", "red")]:
    d = df[df["Resultat"] == res]
    plt.scatter(d["Nb_Produits_Controle"], d["Nb_Defauts"],
                c=couleur, label=res, alpha=0.7)

a, b = np.polyfit(df["Nb_Produits_Controle"], df["Nb_Defauts"], 1)
xs = np.linspace(df["Nb_Produits_Controle"].min(), df["Nb_Produits_Controle"].max(), 100)
plt.plot(xs, a * xs + b, "k--", label="Tendance")

plt.title("Nombre de défauts en fonction du nombre de produits contrôlés")
plt.xlabel("Nb de produits contrôlés")
plt.ylabel("Nb de défauts")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

#%% Graphique 3 : Boîte à moustaches
lignes = sorted(df["Ligne_Production"].unique())
data = [df.loc[df["Ligne_Production"] == l, "Cout_Non_Qualite_DH"] for l in lignes]

plt.figure(figsize=(7, 5))
plt.boxplot(data, tick_labels=lignes, patch_artist=True)
plt.title("Coût de non-qualité par ligne de production")
plt.xlabel("Ligne de production")
plt.ylabel("Coût de non-qualité (DH)")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()