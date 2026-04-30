import pandas as pd
import dask.dataframe as dd
from pyspark.sql import SparkSession
import seaborn as sns
import matplotlib.pyplot as plt

path = "C:/Users/Utente/Desktop/MODULO 2/5/data_local/*.json/"  # Modifica il percorso in base alla posizione dei tuoi file JSON

for file in files:
    data = pd.read_json(file) # Legge ogni file JSON e lo converte in un DataFrame
 
print(data) # Stampa il DataFrame risultante


path_dask = "C:/Users/Utente/Desktop/MODULO 2/5/data_local/json/*.json" # Modifica il percorso in base alla posizione dei tuoi file JSON

data_dask = dd.read_json(path_dask) # Legge i file JSON in un DataFrame Dask

vendite = data_dask.groupby('payment_type').agg({'total': 'sum'}) # Raggruppa i dati per tipo di pagamento e calcola la somma totale per ogni gruppo

media = vendite['total'].mean().compute() # Calcola la media del totale per ogni tipo di pagamento e restituisce il risultato come un numero 

print(media) # Stampa la media del totale per ogni tipo di pagamento
 

spark = SparkSession.builder.appName("TestFinale").getOrCreate() # Crea una sessione Spark

transazioni = spark.read.parquet("C:/Users/Utente/Desktop/MODULO 2/5/data_local/parquet/transactions_batch_*.parquet") # Legge i file Parquet delle transazioni e li unisce in un unico DataFrame Spark

prodotti = spark.read.parquet("C:/Users/Utente/Desktop/MODULO 2/5/data_local/parquet/products_*.parquet") # Legge i file Parquet dei prodotti e li unisce in un unico DataFrame Spark

regioni = spark.read.parquet("C:/Users/Utente/Desktop/MODULO 2/5/data_local/parquet/regions_*.parquet") # Legge i file Parquet delle regioni e li unisce in un unico DataFrame Spark

df_finale = (transazioni
                .join(prodotti, on="product_id", how="left")
                .join(regioni, on="region_id", how="left")
                .select("transaction_id", "total", "payment_type", "category", "region_name", "year") 
) # Crea un DataFrame finale unendo i dati delle transazioni, dei prodotti e delle regioni, selezionando solo le colonne necessarie

df_finale.write.parquet("C:/Users/Utente/Desktop/MODULO 2/5/data_local/parquet/df_finale.parquet", mode="overwrite", partitionBy=["year"]) 
# Salva il DataFrame finale in formato Parquet, partizionando i dati per anno e sovrascrivendo eventuali file esistenti

fatturato_totale_per_categoria = df_finale.groupBy("category").agg({"total": "sum"})
# Raggruppa il DataFrame finale per categoria e calcola la somma totale del fatturato per ogni categoria

fatturato_totale = fatturato_totale_per_categoria.toPandas()
# Converte il DataFrame Spark in un DataFrame Pandas per poter utilizzare Seaborn per la visualizzazione

sns.barplot(data=fatturato_totale, x="category", y="sum(total)")
# Crea un grafico a barre utilizzando Seaborn per visualizzare il fatturato totale per categoria

plt.savefig("C:/Users/Utente/Desktop/MODULO 2/5/data_local/images/fatturato_per_categoria.png")
# Salva il grafico come immagine PNG nella cartella specificata

plt.show()
# Mostra il grafico a video







