import pandas as pd
import numpy as np
# Creazione del DataFrame degli ordini
ordini = pd.DataFrame({
    "ClienteID": np.arange(1, 100_001),
    "ProdottoID": np.random.randint(1, 21, size=100_000),
    "Quantità": np.random.randint(1, 5, size=100_000),
    "DataOrdine": pd.date_range(start="2024-01-01", periods=100_000)
})

ordini.to_csv("ordini.csv", index=False)
# Creazione del DataFrame dei prodotti
prodotti = pd.DataFrame({
    "ProdottoID": np.arange(1, 21),
    "Prezzo": np.random.uniform(10, 500, size=20),
    "Categoria": np.random.choice(["Elettronica", "Abbigliamento", "Casa", "Giocattoli", "Libri"], size=20),
    "Fornitore": np.random.choice(["Fornitore1", "Fornitore2", "Fornitore3", "Fornitore4", "Fornitore5"], size=20)
})
prodotti.to_json("prodotti.json", orient="records")
# Creazione del DataFrame dei clienti
clienti = pd.DataFrame({
    "ClienteID": np.arange(1, 5001),
    "Regione": np.random.choice(["Nord", "Centro", "Sud", "Isole"], size=5000),
    "Segmento": np.random.choice(["Privato", "Azienda"], size=5000)
}) 
clienti.to_csv("clienti.csv", index=False)

# Creazione del DataFrame unificato tramite merge degli ordini, clienti e prodotti
df_unificato = ordini.merge(clienti, on="ClienteID").merge(prodotti, on="ProdottoID")
# Conversione delle colonne in tipi di dati ottimizzati per la memoria
df_unificato["Categoria"] = df_unificato["Categoria"].astype("category")
df_unificato["Regione"] = df_unificato["Regione"].astype("category")
df_unificato["Segmento"] = df_unificato["Segmento"].astype("category")
df_unificato["Fornitore"] = df_unificato["Fornitore"].astype("category")
df_unificato["ProdottoID"] = df_unificato["ProdottoID"].astype("category")
df_unificato["ClienteID"] = df_unificato["ClienteID"].astype("category")
df_unificato["Quantità"] = df_unificato["Quantità"].astype("int16")
# Calcolo della memoria ottimizzata del DataFrame unificato
ottimizzazione_memoria = df_unificato.memory_usage(deep=True).sum() / 1024**2
print(f"Memoria ottimizzata: {ottimizzazione_memoria:.2f} MB")
# Calcolo del valore totale per ogni ordine
df_unificato["Valore_Totale"] = df_unificato["Quantità"] * df_unificato["Prezzo"]

# Filtraggio degli ordini con valore totale superiore a 100
fitro_ordini = df_unificato.loc[df_unificato["Valore_Totale"] > 100, ["ClienteID", "ProdottoID", "Quantità", "Valore_Totale"]]
print(f"Numero di ordini con valore totale superiore a 100: {fitro_ordini.shape[0]}")
print(fitro_ordini)





