import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Input utente
nome = input("Inserisci il tuo nome: ")
eta = int(input("Inserisci la tua età: "))
saldoConto = float(input("Inserisci il saldo del tuo conto bancario: "))
statoVIP = input("Sei un cliente VIP? (True/False): ").lower() == "true"

destinazioniDisponibili = ["Tenerife", "Parigi", "New York", "Tokyo", "Sydney", "Roma"]

DestinazioneEprezzoMedioDelViaggio = {
    "Tenerife": 800.0,
    "Parigi": 1200.0,
    "New York": 2500.0,
    "Tokyo": 3000.0,
    "Sydney": 3500.0,
    "Roma": 1000.0
}

# Classi
class Cliente:
    def __init__(self, nome, eta, vip):
        self.nome = nome
        self.eta = eta
        self.vip = vip

class Viaggio:
    def __init__(self, destinazione, prezzo, durataInGiorni):
        self.destinazione = destinazione
        self.prezzo = prezzo
        self.durataInGiorni = durataInGiorni

# Creazione oggetti
cliente1 = Cliente(nome, eta, statoVIP)
viaggio1 = Viaggio("Roma", 1000, 7)

if cliente1.vip:
    importoFinale = viaggio1.prezzo * 0.9
    print(f"Essendo un cliente VIP, hai diritto a uno sconto del 10%. Il prezzo finale è: {importoFinale} euro.")
else:
    importoFinale = viaggio1.prezzo

print(f"Cliente: {cliente1.nome}, Destinazione: {viaggio1.destinazione}, Prezzo: {importoFinale} euro, Durata: {viaggio1.durataInGiorni} giorni")

# Simulazioni
prenotazioniSimulate = np.random.randint(200, 2000, 100)
prezzoMedioPrenotazioni = np.mean(prenotazioniSimulate)
prezzoMinimoEMassimo = (np.min(prenotazioniSimulate), np.max(prenotazioniSimulate))
deviazioneStandard = np.std(prenotazioniSimulate)
percentualeDiPrenotazioniSopraMedia = np.sum(prenotazioniSimulate > prezzoMedioPrenotazioni) / len(prenotazioniSimulate) * 100

df = pd.DataFrame({
    "Cliente": [f"Cliente_{i}" for i in range(1, 101)],
    "Destinazione": np.random.choice(destinazioniDisponibili, 100),
    "Prezzo": prenotazioniSimulate,
    "Giorno_Partenza": np.random.randint(1, 31, 100),
    "Durata": np.random.randint(3, 15, 100),
    "Incasso": prenotazioniSimulate
})

incassoTotaleAgenzia = df["Incasso"].sum()
print(f"Incasso totale: {incassoTotaleAgenzia} euro")
print("Incasso medio per destinazione:\n", df.groupby("Destinazione")["Incasso"].mean())
print("Top 3 destinazioni più vendute:\n", df["Destinazione"].value_counts().head(3))

# Grafico incasso per destinazione
incasso_per_dest = df.groupby("Destinazione")["Incasso"].sum()
plt.bar(incasso_per_dest.index, incasso_per_dest.values)
plt.xlabel("Destinazioni")
plt.ylabel("Incasso")
plt.title("Incasso per Destinazione")
plt.show()

# Grafico andamento giornaliero
plt.plot(df["Giorno_Partenza"], df["Incasso"])
plt.xlabel("Giorno")
plt.ylabel("Incasso")
plt.title("Andamento dell'Incasso Giornaliero")
plt.show()

# Grafico a torta
valori = df["Destinazione"].value_counts(normalize=True) * 100
plt.pie(valori, labels=valori.index, autopct='%1.1f%%')
plt.title("Percentuale di Prenotazioni per Destinazione")
plt.show()

# Categorie
viaggiPerCategorie = {
    "Europa": ["Parigi", "Roma"],
    "America": ["New York"],
    "Asia": ["Tokyo"],
    "Oceania": ["Sydney"],
    "Africa": ["Tenerife"]
}

incassoTotalePerCategoria = {}
durataMediaDeiViaggiPerCategoria = {}

for categoria, destinazioni in viaggiPerCategorie.items():
    incassoTotalePerCategoria[categoria] = df[df["Destinazione"].isin(destinazioni)]["Incasso"].sum()
    durataMediaDeiViaggiPerCategoria[categoria] = df[df["Destinazione"].isin(destinazioni)]["Durata"].mean()

# Grafico durata media per categoria
plt.bar(durataMediaDeiViaggiPerCategoria.keys(), durataMediaDeiViaggiPerCategoria.values())
plt.xlabel("Categoria")
plt.ylabel("Durata Media (giorni)")
plt.title("Durata Media dei Viaggi per Categoria")
plt.show()

# Salvataggio
df.to_csv("prenotazioni_analizzate.csv", index=False)
print("Analisi completata e dati salvati in 'prenotazioni_analizzate.csv'")
