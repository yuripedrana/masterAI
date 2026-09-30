import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Parte 2 – Importazione con Pandas

df = pd.read_csv("vendite.csv")
print(df)

prime_cinque_righe = df.head(5)
print(prime_cinque_righe)

n_righe_n_colonne = df.shape
print(n_righe_n_colonne)

df.info()


# Parte 3 – Elaborazioni con Pandas

df["Incasso"] = df["Quantita"] * df["Prezzo_unitario"]
print(df)

incasso_totale = df["Incasso"].sum()
print(incasso_totale)

incasso_medio_per_negozio = df.groupby("Negozio")["Incasso"].mean()
print(incasso_medio_per_negozio)

top_3_prodotti_piu_venduti_in_termini_di_quantita = (
    df.groupby("Prodotto")["Quantita"]
    .sum()
    .nlargest(3)
)

print(top_3_prodotti_piu_venduti_in_termini_di_quantita)

raggruppo_per_negozio_e_prodotto = (
    df.groupby(["Negozio", "Prodotto"])["Incasso"]
    .mean()
)

print(raggruppo_per_negozio_e_prodotto)


# Parte 4 – Uso di NumPy

estrazione_quantita = df["Quantita"].to_numpy()
print(estrazione_quantita)

media_quantita = np.mean(estrazione_quantita)
print(media_quantita)

minimo_quantita = np.min(estrazione_quantita)
print(minimo_quantita)

massimo_quantita = np.max(estrazione_quantita)
print(massimo_quantita)

deviazione_standard_quantita = np.std(estrazione_quantita)
print(deviazione_standard_quantita)

percentuale_di_vendite_sopra_media = (
    np.sum(estrazione_quantita > media_quantita)
    / len(estrazione_quantita)
    * 100
)

print(percentuale_di_vendite_sopra_media)


solo_quantita_e_prezzi = np.array(
    df[["Quantita", "Prezzo_unitario"]]
) 

print(solo_quantita_e_prezzi)

incassi_numpy = []

for riga in solo_quantita_e_prezzi:
    incasso = riga[0] * riga[1]
    incassi_numpy.append(incasso)

incassi_numpy = np.array(incassi_numpy)

print(incassi_numpy)

confronto = np.allclose(
    incassi_numpy,
    df["Incasso"].to_numpy()
)

print("I risultati coincidono:", confronto)


# Parte 5 – Visualizzazione con Matplotlib

# Grafico a barre: incasso totale per ogni negozio

incasso_totale_per_negozio = (
    df.groupby("Negozio")["Incasso"].sum()
)

plt.figure(figsize=(10, 6))
plt.bar(
    incasso_totale_per_negozio.index,
    incasso_totale_per_negozio.values
)

plt.xlabel("Negozio")
plt.ylabel("Incasso")
plt.title("Incasso Totale per Negozio")
plt.show()


# Grafico a torta: percentuale di incassi per prodotto

incasso_totale_per_prodotto = (
    df.groupby("Prodotto")["Incasso"].sum()
)

plt.figure(figsize=(10, 6))
plt.pie(
    incasso_totale_per_prodotto.values,
    labels=incasso_totale_per_prodotto.index,
    autopct="%1.1f%%"
)

plt.title("Percentuale di Incassi per Prodotto")
plt.show()


# Grafico a linee: andamento giornaliero degli incassi

incasso_giornaliero = (
    df.groupby("Data")["Incasso"].sum()
)

plt.figure(figsize=(10, 6))
plt.plot(
    incasso_giornaliero.index,
    incasso_giornaliero.values
)

plt.xlabel("Data")
plt.ylabel("Incasso")
plt.title("Andamento Giornaliero degli Incassi")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Parte 6 – Analisi Avanzata

categorie = {
    "Smartphone": "Informatica",
    "Laptop": "Informatica",
    "TV": "Elettrodomestici"
}

df["Categoria"] = df["Prodotto"].map(categorie)

print(df["Categoria"])

incasso_totale_per_categoria = (
    df.groupby("Categoria")["Incasso"].sum()
)

print(incasso_totale_per_categoria)

quantita_media_venduta_per_categoria = (
    df.groupby("Categoria")["Quantita"].mean()
)

print(quantita_media_venduta_per_categoria)

df.to_csv(
    "vendite_analizzate.csv",
    index=False
)


# Parte 7 – Estensioni

incasso_medio_per_categoria = (
    df.groupby("Categoria")["Incasso"].mean()
)

quantita_media_per_categoria = (
    df.groupby("Categoria")["Quantita"].mean()
)

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.bar(
    incasso_medio_per_categoria.index,
    incasso_medio_per_categoria.values
)

ax1.set_xlabel("Categoria")
ax1.set_ylabel("Incasso Medio")

ax2 = ax1.twinx()

ax2.plot(
    quantita_media_per_categoria.index,
    quantita_media_per_categoria.values,
    marker="o"
)

ax2.set_ylabel("Quantità Media Venduta")

plt.title("Incasso Medio e Quantità Media per Categoria")
plt.show()


def top_n_prodotti(n):
    return (
        df.groupby("Prodotto")["Incasso"]
        .sum()
        .nlargest(n)
    )


print(top_n_prodotti(3))

