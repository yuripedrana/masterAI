import numpy as np

nome = str("Mario")
cognome = str("Rossi")
cf = str("RSSMRA80A01H501U")
eta = int(44)
peso = float(75.5)
lista_analisi_effettuate = ["emocromo", "glicemia", "colesterolo", "trigliceridi"]

nome = str("Silvia")
cognome = str("Bianchi")
cf = str("BNCSLV85B41H501Y")
eta = int(38)
peso = float(62.3)
lista_analisi_effettuate = ["immunoglobuline", "proteine sieriche", "patologie epatiche"]

nome = str("Luca")
cognome = str("Verdi")
cf = str("VRDLUC90C12H501Z")
eta = int(33)
peso = float(70.2)
lista_analisi_effettuate = ["emicrania", "allergie", "asma"]

nome = str("Giulia")
cognome = str("Neri")
cf = str("NERGIU92D15H501W")
eta = int(31)
peso = float(68.4)
lista_analisi_effettuate = ["vitamina D", "ferro", "calcio"]

class Paziente:
    def __init__(self, nome, cognome, cf, eta, peso, lista_analisi_effettuate, risultati):
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.eta = eta
        self.peso = peso
        self.lista_analisi_effettuate = lista_analisi_effettuate
        self.risultati = risultati

    def scheda_personale(self):
        return str(f"Nome: {self.nome}\nCognome: {self.cognome}\nCF: {self.cf}")
    
    def statistiche_analisi(self):
        media = np.mean(self.risultati)
        massimo = np.max(self.risultati)
        minimo = np.min(self.risultati)
        deviazione_standard = np.std(self.risultati)
        return {
            "media": media,
            "massimo": massimo,
            "minimo": minimo,
            "deviazione_standard": deviazione_standard
        }
            
class Medico:
    def __init__(self, nome, cognome, specializzazione):
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione

    def visita_paziente(self, paziente):
        return str(f"Il medico {self.nome} {self.cognome} sta visitando il paziente {paziente.nome} {paziente.cognome}")

class Analisi:
    def __init__(self, tipo_di_analisi, risultato):
        self.tipo_di_analisi = tipo_di_analisi
        self.risultato = risultato

    def valuta(self):
        if self.tipo_di_analisi == "emocromo" and self.risultato > 10:
            return str(f"Il risultato dell'analisi {self.tipo_di_analisi} è nella norma.")
        elif self.tipo_di_analisi == "glicemia" and self.risultato > 90:
            return str(f"Il risultato dell'analisi {self.tipo_di_analisi} è nella norma.")
        elif self.tipo_di_analisi == "colesterolo" and self.risultato < 200:
            return str(f"Il risultato dell'analisi {self.tipo_di_analisi} è nella norma.")
        elif self.tipo_di_analisi == "trigliceridi" and self.risultato < 150:
            return str(f"Il risultato dell'analisi {self.tipo_di_analisi} è nella norma.")
        elif self.tipo_di_analisi == "vitamina D" and self.risultato > 30:
            return str(f"Il risultato dell'analisi {self.tipo_di_analisi} è nella norma.")
        else:
            return str(f"Il risultato dell'analisi {self.tipo_di_analisi} non è nella norma.")


    risultati_glicemia_primi_10_pazienti = np.random.randint(70, 130, size=10)
    media_glicemia_primi_10_pazienti = np.mean(risultati_glicemia_primi_10_pazienti)
    max_glicemia_primi_10_pazienti = np.max(risultati_glicemia_primi_10_pazienti)
    min_glicemia_primi_10_pazienti = np.min(risultati_glicemia_primi_10_pazienti)
    deviazione_standard_glicemia_primi_10_pazienti = np.std(risultati_glicemia_primi_10_pazienti)

    print("Risultati glicemia primi 10 pazienti:", risultati_glicemia_primi_10_pazienti)
    print("Media glicemia primi 10 pazienti:", media_glicemia_primi_10_pazienti)
    print("Massimo glicemia primi 10 pazienti:", max_glicemia_primi_10_pazienti)
    print("Minimo glicemia primi 10 pazienti:", min_glicemia_primi_10_pazienti)
    print("Deviazione standard glicemia primi 10 pazienti:", deviazione_standard_glicemia_primi_10_pazienti)


def main():
    medico1 = Medico("Gianni", "Rossi", "Cardiologia")
    medico2 = Medico("Anna", "Verdi", "Neurologia")
    medico3 = Medico("Carlo", "Neri", "Pediatria")

    paziente1 = Paziente(
        "Anna",
        "Rossi",
        "RSSANN80A01H501A",
        45,
        70.5,
        ["glicemia", "colesterolo", "trigliceridi"],
        [95, 180, 120]
    )

    paziente2 = Paziente(
        "Marco",
        "Bianchi",
        "BNCMRC85B41H501B",
        52,
        82.3,
        ["glicemia", "colesterolo", "trigliceridi"],
        [110, 195, 140]

    )

    paziente3 = Paziente(
        "Laura",
        "Verdi",
        "VRDLRA90C12H501C",
        37,
        61.2,
        ["glicemia", "colesterolo", "trigliceridi"],
        [88, 170, 100]

    )

    paziente4 = Paziente(
        "Paolo",
        "Neri",
        "NERPLA92D15H501D",
        60,
        90.4,
        ["glicemia", "colesterolo", "trigliceridi"],
        [125, 210, 160]

    )

    paziente5 = Paziente(
        "Giulia",
        "Ferrari",
        "FRRGLI95D20H501E",
        29,
        58.7,
        ["glicemia", "colesterolo", "trigliceridi"],
        [92, 85, 130]

    )

    pazienti = [paziente1, paziente2, paziente3, paziente4, paziente5]



    for paziente in pazienti:
      print(paziente.scheda_personale())
      print()

    print(medico1.visita_paziente(paziente1))
    print(medico2.visita_paziente(paziente2))
    print(medico3.visita_paziente(paziente3))

    for paziente in pazienti:
        statistica = paziente.statistiche_analisi()
        print("Statistiche analisi per il paziente:", paziente.nome, paziente.cognome)
        print("Risultati:", paziente.risultati)
        print("Media: ", statistica["media"])
        print("Massimo: ", statistica["massimo"])
        print("Minimo: ", statistica["minimo"])
        print("Deviazione standard: ", statistica["deviazione_standard"])

main()