import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

""" Parte 1 – Variabili e Tipi di Dati """
    
nome = "Yuri"
eta = 25
saldo_conto = 1000.0
stato_VIP = False

destinazioni_disponibili = ["Parigi", "Londra", "New York", "Tokyo", "Roma", "Sydney"]
prezzi_medi_per_destinazione = {
    "Parigi": 500.0,
    "Londra": 450.0,
    "New York": 700.0,
    "Tokyo": 800.0,
    "Roma": 400.0,
    "Sydney": 900.0
}

"""Parte 2 – Programmazione ad Oggetti (OOP)
"""

class Cliente:
    def __init__(self, nome, eta, stato_VIP):
        self.nome = nome
        self.eta = eta
        self.stato_VIP = stato_VIP

    def __str__(self):
        return f"Cliente(nome={self.nome}, eta={self.eta}, stato_VIP={self.stato_VIP})"

class Viaggio:
    def __init__(self, destinazione, prezzo, durata_in_giorni):
        self.destinazione = destinazione
        self.prezzo = prezzo
        self.durata_in_giorni = durata_in_giorni

class Prenotazione:
    def __init__(self, cliente, viaggio):
        self.cliente = cliente
        self.viaggio = viaggio

    def calcolo_se_vip(self):
        if self.cliente.stato_VIP:
            return self.viaggio.prezzo * 0.90  # Sconto del 10% per i VIP
        return self.viaggio.prezzo

    def dettagli(self):
        return (f"Prenotazione("
                f"cliente={self.cliente}"
                f"viaggio={self.viaggio}"
                f"prezzo_finale={self.calcolo_se_vip()})")

"""Parte 3 – NumPy"""

prenotazioni_sim = np.random.randint(200, 2001, 100)

prezzo_medio_sim = np.mean(prenotazioni_sim)
prezzo_minimo_sim = np.min(prenotazioni_sim)
prezzo_massimo_sim = np.max(prenotazioni_sim)
deviazione_standard_sim = np.std(prenotazioni_sim)

percentuale_prenotazioni_sopra_media = np.sum(prenotazioni_sim > prezzo_medio_sim) / len(prenotazioni_sim) * 100

print(f"Prezzo medio simulato: {prezzo_medio_sim} \n"
      f"Prezzo minimo simulato: {prezzo_minimo_sim} \n"
      f"Prezzo massimo simulato: {prezzo_massimo_sim} \n"
      f"Deviazione standard simulata: {deviazione_standard_sim} \n"
      f"Percentuale prenotazioni sopra la media: {percentuale_prenotazioni_sopra_media}%")

"""Parte 4 – Pandas"""

df = pd.DataFrame(columns=["Cliente", "Destinazione", "Prezzo", "Giorno_Partenza", "Durata", "Incasso"])


incasso_totale_agenzia = df["Incasso"].sum()
print(f"Incasso totale agenzia: {incasso_totale_agenzia}")

incasso_medio_destinazione = df[df["Destinazione"] == "Tokyo"]["Incasso"].mean()
print(f"Incasso medio per destinazione: {incasso_medio_destinazione}")

top_3_destinazioni_piu_vendute = df["Destinazione"].value_counts().head(3)

print(f"Top 3 destinazioni più vendute: {top_3_destinazioni_piu_vendute}")

"""Parte 5 – Matplotlib"""

plt.figure(figsize=(10, 6))
plt.bar(destinazioni_disponibili, [df[df["Destinazione"] == destinazione]["Incasso"].sum() for destinazione in destinazioni_disponibili])
plt.xlabel('Destinazioni')
plt.ylabel('Incasso Totale')
plt.title('Distribuzione Incasso Totale per Destinazione')
plt.show()

plt.figure(figsize=(10, 6))
date = pd.date_range(start="2024-01-01", periods=30, freq="D")
incassi_giornalieri = [df[df["Giorno_Partenza"] == giorno]["Incasso"].sum() for giorno in date]
plt.plot(date, incassi_giornalieri)
plt.xlabel('Tempo')
plt.ylabel('Incasso Totale') 
plt.title('Andamento Incasso Totale Agenzia nel Tempo')
plt.show()

plt.figure(figsize=(10, 6))
vendite_per_destinazione = df["Destinazione"].value_counts()
plt.pie(vendite_per_destinazione, labels=vendite_per_destinazione.index, autopct='%1.1f%%')
plt.title('Distribuzione Incasso per Destinazione')
plt.show()

"""Parte 6 – Analisi Avanzata"""

categorie = {
    "Parigi": "Europa",
    "Roma": "Europa",
    "Londra": "Europa",
    "Tokyo": "Asia",
    "New York": "America"
}
df["Categorie"] = df["Destinazione"].map(categorie)
incasso_medio_per_categorie = df.groupby("Categorie")["Incasso"].mean()
durata_media_viaggi_categorie = df.groupby("Categorie")["Durata"].mean()
salvtaggio_df_csv = df.to_csv("prenotazioni_analizzate.csv", index=False)

"""Parte 7 – Estensioni"""


def clienti_con_piu_prenotazioni(n):
    return df["Cliente"].value_counts().head(n)

fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.bar(incasso_medio_per_categorie.index, incasso_medio_per_categorie.values)
ax1.set_xlabel('Categorie')
ax1.set_ylabel('Incasso Medio')
ax2 = ax1.twinx()
ax2.set_ylabel('Durata Media Viaggi')
ax1.set_title('Distribuzione Incasso Medio per Categorie')
ax2.plot(durata_media_viaggi_categorie.index, durata_media_viaggi_categorie.values, color='red', marker='o', linestyle='--')
plt.show()