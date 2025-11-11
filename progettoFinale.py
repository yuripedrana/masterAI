import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("vendite.csv")

print("Prime 5 righe del DataFrame:")
print(df.head())

print("N.ro righe e colonne del DataFrame:")
print(df.shape) 

print("Informazioni sul DataFrame:")
print(df.info())

df["Incasso"] = df["Quantita"] * df["Prezzo_unitario"]

incasso_totale = df["Incasso"].sum()
print(f"Incasso totale: {incasso_totale} euro")

incassoMedioPerNegozio = df.groupby("Negozio")["Incasso"].mean()
print("Incasso medio per negozio:\n", incassoMedioPerNegozio)

top3_prodotti = df.groupby("Prodotto")["Quantita"].sum().nlargest(3)
print("Top 3 prodotti più venduti:\n", top3_prodotti)

incasso_medio = df.groupby(["Negozio", "Prodotto"])["Incasso"].mean()
print("Incasso medio per negozio e prodotto:\n", incasso_medio)

colonnaQuantita = df["Quantita"].to_numpy()
mediaQuantita = np.mean(colonnaQuantita)
minimaQuantita = np.min(colonnaQuantita)
massimaQuantita = np.max(colonnaQuantita)
deviazioneStandardQuantita = np.std(colonnaQuantita)
print(f"Quantità - Media: {mediaQuantita}, Min: {minimaQuantita}, Max: {massimaQuantita}, Deviazione Standard: {deviazioneStandardQuantita}")
percentualeDiVenditeSopraMedia = np.sum(colonnaQuantita > mediaQuantita) / len(colonnaQuantita) * 100
print(f"Percentuale di vendite sopra la media: {percentualeDiVenditeSopraMedia}%")


array2D = df[["Quantita", "Prezzo_unitario"]].to_numpy()
incassi_calcolati = array2D[:, 0] * array2D[:, 1]
print("Incassi calcolati (Quantità * Prezzo_unitario):\n", incassi_calcolati)

incasso_per_negozio = df.groupby("Negozio")["Incasso"].sum()

plt.bar(incasso_per_negozio.index, incasso_per_negozio.values)
plt.xlabel("Negozio")
plt.ylabel("Incasso Totale")
plt.title("Incasso Totale per Negozio")
plt.show()

incasso_per_prodotto = df.groupby("Prodotto")["Incasso"].sum()
plt.pie(incasso_per_prodotto.values, labels=incasso_per_prodotto.index, autopct='%1.1f%%')
plt.title("Distribuzione Incasso per Prodotto")
plt.show()


df.groupby("Negozio")["Incasso"].sum().plot(kind='bar', title='Incasso Totale per Negozio')
plt.xlabel("Negozio")
plt.ylabel("Incasso Totale")
plt.show()

df["Categoria"] = df["Prodotto"].apply(lambda x: "Elettronica" if x in ["TV", "Smartphone", "Laptop"] else "Altro")
print("DataFrame con nuova colonna 'Categoria':")
print(df.head())

incassoTotalePerCategoria = df.groupby("Categoria")["Incasso"].sum()
print("Incasso totale per categoria:\n", incassoTotalePerCategoria)

quantitaMediaVendutaPerCategoria = df.groupby("Categoria")["Quantita"].mean()
print("Quantità media venduta per categoria:\n", quantitaMediaVendutaPerCategoria)

df.to_csv("vendite_analizzate.csv", index=False)

incassoMedioPerCategoria = df.groupby("Categoria")["Incasso"].mean()
plt.bar(incassoMedioPerCategoria.index, incassoMedioPerCategoria.values)
plt.xlabel("Categoria")
plt.ylabel("Incasso Medio")
plt.title("Incasso Medio per Categoria")
plt.show()

lineQuantitaMediaVenduta = df.groupby("Categoria")["Quantita"].mean()
plt.plot(lineQuantitaMediaVenduta.index, lineQuantitaMediaVenduta.values, marker='o')
plt.xlabel("Categoria")
plt.ylabel("Quantità Media Venduta")
plt.title("Quantità Media Venduta per Categoria")
plt.show()



def top_n_prodotti(n):
	return df.groupby("Prodotto")["Incasso"].sum().nlargest(n)

