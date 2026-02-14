import pandas as pd
import numpy as np

data = {
    'Prodotto': ['TelEFONO ', '  TABLET  ', None, '  TABLET  ', ' mOuSe '],
    'Data_di_vendita': ['2020-01-01', '2023-02-15', '2023-03-20', None, '2023-00-25'],
    'Prezzo': [None, 50, 150, 0, 80],
    'Quantita': [10, 20, 5, 15, 25],
}


df = pd.DataFrame(data)

print('Prime righe:', df.head()) #prime righe del DataFrame
print('Informazioni sul DataFrame:', df.info()) #informazioni sul DataFrame
print('Statistiche descrittive:', df.describe()) #statistiche descrittive del DataFrame

df['Prodotto'] = df['Prodotto'].map(lambda x: x.strip().capitalize().replace("  ", " ") if pd.notnull(x) else x) 
#Rimuove spazi bianchi, capitalizza la prima lettera e sostituisce spazi doppi con uno spazio singolo nella colonna 'Prodotto'
df['Data_di_vendita'] = pd.to_datetime(df['Data_di_vendita'], errors='coerce')
#Converte la colonna 'Data_di_vendita' in formato datetime, sostituendo i valori non convertibili con NaT (Not a Time)
df['Prezzo'] = df['Prezzo'].fillna(df['Prezzo'].median())
#Sostituisce i valori mancanti nella colonna 'Prezzo' con la mediana dei prezzi

df = df.dropna().drop_duplicates()
#Rimuove le righe con valori mancanti e le righe duplicate dal DataFrame

Q1_prezzo = df['Prezzo'].quantile(0.25)
Q3_prezzo = df['Prezzo'].quantile(0.75)
#Calcola il primo quartile (Q1) e il terzo quartile (Q3) per la colonna 'Prezzo' al fine di identificare gli outlier

IQR_prezzo = Q3_prezzo - Q1_prezzo
lower_bound_prezzo = Q1_prezzo - 1.5 * IQR_prezzo
upper_bound_prezzo = Q3_prezzo + 1.5 * IQR_prezzo 
#Calcola l'intervallo interquartile (IQR) e i limiti inferiore e superiore per identificare gli outlier nella colonna 'Prezzo'  

#Ricavo totale
df['Ricavo'] = df['Prezzo'] * df['Quantita']

#totale vendite per prodotto
totale_per_prodotto = df.groupby('Prodotto')['Ricavo'].sum()

#prodotto più venduto
prodotto_piu_venduto = totale_per_prodotto.idxmax()

#prodotto meno venduto
prodotto_meno_venduto = totale_per_prodotto.idxmin()

#vendite medie giornaliere
df['Vendite_Medie_Giornaliere'] = df['Ricavo'] / df['Data_di_vendita'].dt.days_in_month

print(df)
print('Totale per prodotto:\n', totale_per_prodotto)
print('Prodotto più venduto:', prodotto_piu_venduto)
print('Prodotto meno venduto:', prodotto_meno_venduto)

