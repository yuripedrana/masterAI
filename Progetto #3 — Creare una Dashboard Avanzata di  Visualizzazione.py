
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, CheckButtons, RadioButtons
import matplotlib.gridspec as gridspec
import seaborn as sns

# Creazione dataset
np.random.seed(42)

# Creazione delle date per gli ordini
dates = pd.date_range(
    start="2022-01-01",
    end="2025-12-31",
    periods=100
)
# Creazione del DataFrame degli ordini
ordini = pd.DataFrame({
    "Order_Date": dates,
    "Ship_Date": dates + pd.Timedelta(days=1), # La data di spedizione è un giorno dopo la data dell'ordine
    "Categoria": np.random.choice(
        ["Furniture", "Technology", "Office Supplies"], size=100
    ),
    "Sub_Categoria": np.random.choice(
        ["Chairs", "Phones", "Binders"], size=100
    ),
    "Vendite": np.random.randint(100, 500, size=100),
    "Profitto": np.random.randint(50, 300, size=100),
    "Region": np.random.choice(
        ["North", "South", "East", "West"], size=100
    ),
    "State": np.random.choice(
        ["California", "Texas", "New York", "Florida"], size=100
    ),
    "Quantity": np.random.randint(1, 20, size=100),
})

# da stringa a datetime
ordini["Order_Date"] = pd.to_datetime(ordini["Order_Date"])
ordini["Ship_Date"] = pd.to_datetime(ordini["Ship_Date"])

# Rimozione dei valori mancanti e dei duplicati
ordini = ordini.dropna().drop_duplicates().copy()

# Aggiunta dell'anno dell'ordine
ordini["Year"] = ordini["Order_Date"].dt.year



# totale per anno per vendite e profitti
totale_per_anno = ordini.groupby("Year")[["Vendite", "Profitto"]].sum()

# top 5 sottocategorie per vendite
top_5_sotto_categorie = (
    ordini.groupby("Sub_Categoria")[["Vendite", "Profitto"]]
    .sum()
    .nlargest(5, "Vendite")
)

# Grafici statici delle analisi richieste
fig_eda, axes_eda = plt.subplots(1, 2, figsize=(12, 5))

# grafico delle vendite e dei profitti per anno
totale_per_anno.plot(
    kind="bar",
    ax=axes_eda[0],
    color=["blue", "green"]
)

# settaggio dei titoli e delle etichette degli assi per il grafico delle vendite e dei profitti per anno
axes_eda[0].set_title("Vendite e profitti per anno")
axes_eda[0].set_xlabel("Anno")
axes_eda[0].set_ylabel("Importo (€)")
axes_eda[0].tick_params(axis="x", rotation=0)

# grafico delle top 5 sottocategorie per vendite
top_5_sotto_categorie["Vendite"].plot(
    kind="bar",
    ax=axes_eda[1],
    color="orange"
)

# settaggio dei titoli e delle etichette degli assi per il grafico delle top 5 sottocategorie per vendite
axes_eda[1].set_title("Top 5 sottocategorie per vendite")
axes_eda[1].set_xlabel("Sottocategoria")
axes_eda[1].set_ylabel("Vendite (€)")
axes_eda[1].tick_params(axis="x", rotation=30)

# visualizzazione dei grafici statici
fig_eda.tight_layout()


# preparazione dei dati per la dashboard interattiva
anni = sorted(ordini["Year"].unique()) # Lista degli anni presenti nei dati
regioni = ["North", "South", "East", "West"] # Lista delle regioni presenti nei dati

fig = plt.figure(figsize=(15, 7))
gs = gridspec.GridSpec(1, 3, figure=fig)

ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[0, 2])

fig.subplots_adjust(
    left=0.22, bottom=0.22, top=0.88, right=0.97, wspace=0.45
)

# Slider per selezionare l'anno
slider_ax = fig.add_axes([0.28, 0.10, 0.40, 0.04])

slider = Slider(
    slider_ax,
    "Anno",
    valmin=min(anni),
    valmax=max(anni),
    valinit=min(anni),
    valstep=anni
)

# Checkbox per scegliere le metriche
checkbox_ax = fig.add_axes([0.02, 0.58, 0.16, 0.12])

check = CheckButtons(
    checkbox_ax,
    ["Totale Vendite", "Profitto"],
    [True, True]
)

# Radio buttons per la regione
radio_ax = fig.add_axes([0.02, 0.78, 0.16, 0.15])

radio = RadioButtons(
    radio_ax,
    regioni,
    active=0
)

# Radio buttons per la metrica della heatmap
metric_ax = fig.add_axes([0.02, 0.38, 0.16, 0.12])

metric = RadioButtons(
    metric_ax,
    ["Totale Vendite", "Profitto"],
    active=0
)

# Pulsante per salvare la dashboard
button_ax = fig.add_axes([0.78, 0.08, 0.12, 0.06])

button = Button(
    button_ax,
    "Salva",
    color="lightblue"
)


# funzioni di aggiornamento per la dashboard interattiva

def slider_update(val):
    anno_selezionato = int(slider.val)
    regione_selezionata = radio.value_selected

    dati_filtrati = ordini[
        (ordini["Year"] == anno_selezionato) &
        (ordini["Region"] == regione_selezionata)
    ]

    ax1.clear()
    ax2.clear()

    if check.get_status()[0]:
        vendite = dati_filtrati["Vendite"].sum()

        ax1.bar(
            ["Vendite"],
            [vendite],
            color="blue"
        )
        ax1.set_title("Vendite")
        ax1.set_ylabel("Importo (€)")
    else:
        ax1.set_title("Vendite nascoste")

    if check.get_status()[1]:
        profitto = dati_filtrati["Profitto"].sum()

        ax2.bar(
            ["Profitto"],
            [profitto],
            color="green"
        )
        ax2.set_title("Profitto")
        ax2.set_ylabel("Importo (€)")
    else:
        ax2.set_title("Profitto nascosto")

    fig.canvas.draw_idle()

    metric_update(metric.value_selected)


# controllo delle checkbox

def check_update(label):
    slider_update(slider.val)


# controllo della regione

def radio_update(label):
    slider_update(slider.val)


# controllo della metrica della heatmap

def metric_update(label):
    anno_selezionato = int(slider.val)
    regione_selezionata = radio.value_selected

    dati_filtrati = ordini[
        (ordini["Year"] == anno_selezionato) &
        (ordini["Region"] == regione_selezionata)
    ]

    ax3.clear()

    if len(dati_filtrati) >= 2:
        if label == "Totale Vendite":
            colonne = ["Vendite", "Profitto", "Quantity"]
            titolo = "Correlazioni - Vendite"
        else:
            colonne = ["Profitto", "Vendite", "Quantity"]
            titolo = "Correlazioni - Profitto"

        correlazioni = dati_filtrati[colonne].corr()

        sns.heatmap(
            correlazioni,
            annot=True,
            cmap="coolwarm",
            vmin=-1,
            vmax=1,
            ax=ax3
        )

        ax3.set_title(titolo)
    else:
        ax3.text(
            0.5, 0.5,
            "Dati insufficienti",
            ha="center",
            va="center",
            transform=ax3.transAxes
        )

    fig.canvas.draw_idle()


# controllo del pulsante di salvataggio

def save_figure(event):
    fig.savefig("dashboard_vendite.png", dpi=150, bbox_inches="tight")
    print("Dashboard salvata come 'dashboard_vendite.png'")


# Collegamento widget e callback
slider.on_changed(slider_update)
check.on_clicked(check_update)
radio.on_clicked(radio_update)
metric.on_clicked(metric_update)
button.on_clicked(save_figure)

# Visualizzazione iniziale
slider_update(slider.val)

plt.show()
