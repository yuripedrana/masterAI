import pandas as pd
import numpy as np

dataset = {
    "Data_Vendita": ["2024-01-01", "2024-02-15", "2024-03-10", "2024-04-05", "2024-05-01"],
    "Prodotto": ["La ptop", "Gonn a", "Ane llo", "Trucc o", "T rucco"],
    "Vendite": [5, 10, None, 8, None],
    "Prezzo": [1000, 50, 200, 300, 300],
}

df = pd.DataFrame(dataset)

prime_righe = df.head()
print(prime_righe)

struttura_df = df.info()
print(struttura_df)

statistiche_descrittive = df.describe()
print(statistiche_descrittive)

# Pulizia dei dati
df["Data_Vendita"] = pd.to_datetime(df["Data_Vendita"], errors='coerce')
df["Prodotto"] = df["Prodotto"].map(lambda x: x.strip().replace(" ", "").capitalize() if pd.notnull(x) else x)
df["Vendite"] = df["Vendite"].fillna(0)
df["Prezzo"] = df["Prezzo"].fillna(0)

# Rimozione delle righe duplicate
df = df.drop_duplicates()

# Verifica dei dati puliti
print(df)

vendite_totale_per_prodotto = df.groupby("Prodotto")["Vendite"].sum()
print(vendite_totale_per_prodotto)

prodotto_piu_venduto = vendite_totale_per_prodotto.idxmax()
print(prodotto_piu_venduto)

prodotto_meno_venduto = vendite_totale_per_prodotto.idxmin()
print(prodotto_meno_venduto)

vendite_giornaliere = df.groupby("Data_Vendita")["Vendite"].sum()
print(vendite_giornaliere)


