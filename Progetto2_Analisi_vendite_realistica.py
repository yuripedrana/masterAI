import pandas as pd
import numpy as np
import time

righe = 100_000

ordini = pd.DataFrame({
    "Cliente_ID": np.arange(1, righe + 1),
    "Prodotto_ID": np.arange(1, righe + 1),
    "Quantità": np.random.randint(1, 20, righe),
    "Data_Ordine": pd.to_datetime("2024-01-01") + pd.to_timedelta(np.random.randint(0, 365, righe), unit='D')
})
 #Creaazione del DataFrame "ordini" con 100.000 righe, contenente informazioni sui clienti, prodotti, quantità e date degli ordini.
ordini.to_csv("ordini.csv", index=False)
#salvataggio del DataFrame "ordini" in un file CSV chiamato "ordini.csv" senza includere l'indice.
prodotti = pd.DataFrame({
    "Prodotto_ID": np.arange(1, 21),
    "Prezzo": np.random.uniform(10, 100, 20),
    "Categoria": np.random.choice(["Elettronica", "Abbigliamento", "Casa", "Giocattoli"], 20),
    "Fornitore": np.random.choice(["F1", "F2", "F3", "F4"], 20),
})
#Creazione del DataFrame "prodotti" con 20 righe, contenente informazioni sui prodotti, prezzi, categorie e fornitori.
prodotti.to_json("prodotti.json", orient="records", lines=True)
#Salvataggio del DataFrame "prodotti" in un file JSON chiamato "prodotti.json" con orientamento "records" e scrittura su più righe.
righe_clienti = 5_000

clienti = pd.DataFrame({
    "Cliente_ID": np.arange(1, righe_clienti + 1),
    "Regione": np.random.choice(["Nord", "Sud", "Est", "Ovest"], righe_clienti),
    "Segmento": np.random.choice(["A", "B", "C", "D"], righe_clienti)
})
#Creazione del DataFrame "clienti" con 5.000 righe, contenente informazioni sui clienti, regioni e segmenti.
clienti.to_csv("clienti.csv", index=False)
#Salvataggio del DataFrame "clienti" in un file CSV chiamato "clienti.csv" senza includere l'indice.
start_esecuzione = time.time()
df_ordini_prodotti = pd.merge(ordini, prodotti, on="Prodotto_ID", how="left")
df_finale = pd.merge(df_ordini_prodotti, clienti, on="Cliente_ID", how="left")
end_esecuzione = time.time()
#Unione dei DataFrame "ordini" e "prodotti" sulla colonna "Prodotto_ID" utilizzando un merge di tipo "left", e successivamente unione del risultato con il DataFrame "clienti" sulla colonna "Cliente_ID" sempre con un merge di tipo "left". Il tempo di esecuzione di queste operazioni viene misurato.
start_ottimizzazione = time.time()
df_finale.memory_usage(deep=True).sum() / (1024 ** 2)

df_finale["Cliente_ID"] = df_finale["Cliente_ID"].astype("int32")
df_finale["Quantità"] = df_finale["Quantità"].astype("int8")
df_finale["Data_Ordine"] = pd.to_datetime(df_finale["Data_Ordine"])
df_finale['Prodotto_ID'] = df_finale['Prodotto_ID'].astype('category')
df_finale['Categoria'] = df_finale['Categoria'].astype('category')
df_finale['Fornitore'] = df_finale['Fornitore'].astype('category')
df_finale['Regione'] = df_finale['Regione'].astype('category')
df_finale['Segmento'] = df_finale['Segmento'].astype('category')

df_finale.memory_usage(deep=True).sum() / (1024 ** 2)
end_ottimizzazione = time.time()
#Ottimizzazione del DataFrame "df_finale" riducendo l'utilizzo di memoria. Vengono convertite le colonne "Cliente_ID" e "Quantità" in tipi di dati più efficienti (int32 e int8 rispettivamente), la colonna "Data_Ordine" viene convertita in formato datetime, e le colonne "Prodotto_ID", "Categoria", "Fornitore", "Regione" e "Segmento" vengono convertite in tipo "category". Il tempo di ottimizzazione viene ancora misurato.
df_finale.info(memory_usage="deep")
df_finale.describe()
df_finale.isna().sum()
#Vengono visualizzate informazioni sul DataFrame "df_finale", inclusa l'utilizzo di memoria, statistiche descrittive e il conteggio dei valori mancanti per ogni colonna.
print(f"Tempo di esecuzione: {end_esecuzione - start_esecuzione:.2f} secondi")
print(f"Tempo di ottimizzazione: {end_ottimizzazione - start_ottimizzazione:.2f} secondi")
#Vengono stampati i tempi di esecuzione e ottimizzazione in secondi, formattati con due decimali.
df_finale["ValoreTotale"] = df_finale["Quantità"] * df_finale["Prezzo"]
df_filtrato = df_finale[df_finale["ValoreTotale"] > 100].copy()
#Viene creata una nuova colonna "ValoreTotale" nel DataFrame "df_finale" calcolando il prodotto tra le colonne "Quantità" e "Prezzo". Successivamente, viene filtrato il DataFrame per mantenere solo le righe in cui "ValoreTotale" è maggiore di 100, creando un nuovo DataFrame chiamato "df_filtrato".
ordini_sopra_100 = df_filtrato.groupby("Cliente_ID")["ValoreTotale"].sum().reset_index()
clienti_sopra_100 = pd.merge(clienti, ordini_sopra_100, on="Cliente_ID", how="inner")
print("Clienti con ordini totali superiori a 100:")
print(clienti_sopra_100)
print("Ordini con valore totale superiore a 100:")
print(ordini_sopra_100)
#Viene raggruppato il DataFrame "df_filtrato" per "Cliente_ID" e viene calcolata la somma di "ValoreTotale" per ogni cliente, creando un nuovo DataFrame chiamato "ordini_sopra_100". Successivamente, viene effettuata un'unione (merge) tra il DataFrame "clienti" e "ordini_sopra_100" sulla colonna "Cliente_ID" utilizzando un merge di tipo "inner", creando un nuovo DataFrame chiamato "clienti_sopra_100" che contiene solo i clienti con ordini totali superiori a 100.

