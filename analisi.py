import numpy as np

class Paziente:
    def __init__(self, nome, cognome, codice_fiscale, eta, peso, analisi_effettuate):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.eta = eta
        self.peso = peso
        self.analisi_effettuate = analisi_effettuate
        self.risultati_analisi = np.array([])

    def scheda_personale(self):
        return f"Nome: {self.nome}, Cognome: {self.cognome}, Codice Fiscale: {self.codice_fiscale}, Età: {self.eta}"
    
class Medico:
    def __init__(self, nomeMedico, cognomeMedico, specializzazione):
        self.nomeMedico = nomeMedico
        self.cognomeMedico = cognomeMedico
        self.specializzazione = specializzazione

    def visita_paziente(self, paziente):
        return f"Visita effettuata da: {self.nomeMedico} {self.cognomeMedico} al paziente {paziente.nome} {paziente.cognome}"
    

class Analisi:
    def __init__(self, tipo_analisi, risultati):
        self.tipo_analisi = tipo_analisi
        self.risultati = risultati

    def mostra_risultati(self):
        return f"Tipo di analisi: {self.tipo_analisi}, Risultati: {self.risultati}"
    
    def valuta(self):
        valutazione = []
        for risultato in self.risultati:
            if risultato < 50:
                valutazione.append("Basso")
            elif 50 <= risultato <= 100:
                valutazione.append("Normale")
            else:
                valutazione.append("Alto")
        return valutazione

    def statistiche_analisi(self):
        medio = np.median(self.risultati)
        massimo = np.max(self.risultati)
        minimo = np.min(self.risultati)
        deviazione_standard = np.std(self.risultati)

        return {
            "Media": medio,
            "Massimo": massimo,
            "Minimo": minimo,
            "Deviazione Standard": deviazione_standard
        }

def main():
    medici = []
    pazienti = []

    medico1 = Medico("Dr. Luigi", "Verdi", "Cardiologia")
    medico2 = Medico("Dr. Maria", "Rossi", "Endocrinologia")
    medico3 = Medico("Dr. Anna", "Bianchi", "Ematologia")

    medici.extend([medico1, medico2, medico3])

    paziente1 = Paziente("Mirko", "Verdi", "MRVRDK80A01H501U", 25, 90.2, ["emocromo", "glicemia","diabete"])
    paziente2 = Paziente("Marco", "Rossi", "MRCRSS80A01H501U", 30, 70.5, ["colesterolo", "glicemia","diabete"])
    paziente3 = Paziente("Luca", "Bianchi", "LCBNCH80A01H501U", 28, 80.0, ["emocromo", "colesterolo","glicemia"])
    paziente4 = Paziente("Maria", "Neri", "GLNRI80A01H501U", 32, 65.3, ["emocromo", "glicemia","diabete", "colesterolo"])
    paziente5 = Paziente("Giulia", "Russo", "GLRRSU80A01H501U", 29, 68.4, ["emocromo", "glicemia"])

    pazienti.extend([paziente1, paziente2, paziente3, paziente4, paziente5])

    if(len(medici) < 3 or len(pazienti) < 5):
        print("Errore: Numero insufficiente di medici o pazienti.")
        return
    
    for paziente in pazienti:
        print(paziente.scheda_personale())
        for medico in medici:
            print(medico.visita_paziente(paziente))
        
            paziente.risultati_analisi = np.random.randint(40, 130, size=5)

        analisi = Analisi("Generale", paziente.risultati_analisi)
        print(analisi.mostra_risultati())
        print("Valutazione:", analisi.valuta())
        print("Statistiche:", analisi.statistiche_analisi())


if __name__ == "__main__":
    main()