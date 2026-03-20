import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import datetime
from matplotlib.widgets import Slider

df = pd.DataFrame({
    'Data_ordine': [
        '02-01-2004', '03-01-2004', '04-01-2004',
        '02-01-2005', '03-01-2005', '04-01-2005',
        '02-01-2006', '03-01-2006', '04-01-2006'
        ],
    'Data_spedizione': [
        '05-01-2004', '06-01-2004', '07-01-2004',
        '05-01-2005', '06-01-2005', '07-01-2005',
        '05-01-2006', '06-01-2006', '07-01-2006'
    ],
    'Categorie_prodotti': [
        "Furniture", "Office Supplies", "Technology",
        "Furniture", "Office Supplies", "Technology",
        "Furniture", "Office Supplies", "Technology"],

    'Subcategorie_prodotti': [
        "Tables", "Phone", "Printers",
        "Tables", "Phone", "Printers",
        "Tables", "Phone", "Printers"
    ],
    'Vendite': [100, 150, 200, 
                200, 250, 300,
                400, 450, 350],
    'Profitti': [1100, 1200, 1300, 
                1400, 1500, 1600, 
                1700, 1800, 1900],
    'Regioni': [
        "Lombardia", "Berlino", "Tenerife",
        "Lombardia", "Berlino", "Tenerife",
        "Lombardia", "Berlino", "Tenerife"
    ],
    'Stato': [
        "Italia", "Germania", "Spagna",
        "Italia", "Germania", "Spagna",
        "Italia", "Germania", "Spagna"
    ],
    'Quantità_Venduta': [1000, 1500, 2000, 
                        3000, 3500, 4000, 
                        5000, 5500, 6000]
})

# Convertire le colonne 'Data_ordine' e 'Data_spedizione' in formato datetime
df['Data_ordine'] = pd.to_datetime(df['Data_ordine'])
df['Data_spedizione'] = pd.to_datetime(df['Data_spedizione'])

# Pulizia dei dati: rimozione di valori nulli e duplicati
df_pulito = df.dropna().drop_duplicates().reset_index(drop=True)

# Crezione nuova colonna Anno dalla colonna Data_ordine
df_pulito['Anno'] = df_pulito['Data_ordine'].dt.year

# Totale vendite e profitti per anno
totale_vendite_per_anno = df_pulito.groupby('Anno')['Vendite'].sum()
totale_profitti_per_anno = df_pulito.groupby('Anno')['Profitti'].sum()

# Top 5 sottocategorie piu vendute
top_sottocategorie = df_pulito.groupby('Subcategorie_prodotti')['Quantità_Venduta'].sum().nlargest(5)

# Mappa interattiva delle vendite 
vendite = df_pulito.groupby('Stato')['Vendite'].sum().reset_index()
fig, ax = plt.subplots()
sns.barplot(x='Stato', y='Vendite', data=vendite, ax=ax)
ax.set_title('Vendite per Stato')
ax.set_xlabel('Stato')
ax.set_ylabel('Vendite')

slider_ax = plt.axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(slider_ax, 'Anno', df_pulito['Anno'].min(), df_pulito['Anno'].max(), valinit=df_pulito['Anno'].min(), valstep=1)

def update_slider(val):
    anno_selezionato = int(slider.val)
    vendite = df_pulito[df_pulito['Anno'] == anno_selezionato].groupby('Stato')['Vendite'].sum().reset_index()
    ax.clear()
    sns.barplot(x='Stato', y='Vendite', data=vendite, ax=ax)
    ax.set_title(f'Vendite per Stato - Anno {int(anno_selezionato)}')
    ax.set_xlabel('Stato')
    ax.set_ylabel('Vendite')
    fig.canvas.draw_idle()
    
slider.on_changed(update_slider)
plt.show()