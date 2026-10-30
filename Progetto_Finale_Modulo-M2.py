import pandas as pd
import dask.dataframe as dd
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum
import seaborn as sns
import matplotlib.pyplot as plt
import glob

# o Task: Scrivi uno script che legge i file JSON uno alla volta (ciclo for), calcola la somma della colonna amount per ogni file e stampa il totale generale alla fine.
file = glob.glob("./Progetto_Finale_M2/data_local/json/*.jsonl")
totale_generale = 0
for path in file:
    df = pd.read_json(path, lines=True)
    totale_generale += df["amount"].sum()

print("Totale generale:", totale_generale)

# 2. La soluzione Dask: Utilizza la libreria dask.dataframe. 
# o Task: Leggi tutti i file JSON in un colpo solo usando il carattere jolly (*.json).
# o Task: Raggruppa le vendite per payment_type e calcola la media degli importi.
# Esegui il calcolo con .compute() e stampa il risultato.

df_dask = dd.read_json("./Progetto_Finale_M2/data_local/json/*.jsonl")
df_grouped = df_dask.groupby("payment_type")["amount"].mean().compute()
print(df_grouped)


# ESERCIZIO 2: Pipeline ETL con PySpark 
# Obiettivo: Unire fonti dati diverse (Data Warehousing).

spark = SparkSession.builder.appName("ETL Pipeline").getOrCreate()

# Caricamento tre tabelle parquet
df_transazioni = spark.read.parquet("./Progetto_Finale_M2/data_local/parquet/transactions_batch_*.parquet")
df_prodotti = spark.read.parquet("./Progetto_Finale_M2/data_local/parquet/products.parquet")
df_regioni = spark.read.parquet("./Progetto_Finale_M2/data_local/parquet/regions.parquet")

# Unione delle tabelle delle transazioni con i prodotti per avere la categoria
categoria = df_transazioni.join(df_prodotti, df_transazioni["product_id"] == df_prodotti["product_id"], "inner")

# Unione con le regioni per avere il nome della regione
nome_regione = categoria.join(df_regioni, categoria["region_id"] == df_regioni["region_id"], "inner")

df_pulito = nome_regione.select("transaction_id", "region_name", "category", "amount", "year")

# Salvataggio del DataFrame pulito in formato Parquet, partizionando per anno

df_pulito.write.parquet("./Progetto_Finale_M2/data_local/processed_sales/df_pulito.parquet", partitionBy=["year"], mode="overwrite")

print("File salvato correttamente.")

# Calcolo del fatturato totale per categoria
fatturato = df_pulito.groupBy("category").agg(sum("amount").alias("amount"))
print(fatturato)

# Azione con toPandas per portare questo risultato aggregato 
risultato_agg = fatturato.toPandas()
print(risultato_agg)

# Barchart per mostrare il grafico a barre del fatturato per categoria
sns.barplot(x="category", y="amount", data=risultato_agg)
plt.title("Fatturato per categoria")
plt.xlabel("Categoria")
plt.ylabel("Fatturato")

# Salvataggio del grafico in formato PNG
plt.savefig("./Progetto_Finale_M2/data_local/processed_sales/fatturato_per_categoria.png")
plt.show()

# Mostra il fatturato per categoria in formato tabellare PySpark
fatturato.show()