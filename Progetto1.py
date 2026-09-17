titolo = str(input("Inserisci il titolo del libro: "))
numero_copie = int(input("Inserisci il numero di copie: "))
prezzo_medio_libro = float(input("Inserisci il prezzo medio del libro: "))
stato_disponibilita = bool(int(input("Inserisci lo stato di disponibilità (1 per disponibile, 0 per non disponibile): ")))

print("Titolo:", titolo, "Numero copie:", numero_copie, "Prezzo medio:", prezzo_medio_libro, "Disponibilità:", stato_disponibilita)

titoli_libri = ["Divina Commedia", "Il Nome della Rosa", "I Promessi Sposi", "La coscienza di Zeno", "Il Gattopardo"]

titoli_copie = {titolo: numero_copie for titolo in titoli_libri}

print("Titoli e copie:", titoli_copie)

utenti_registrati = set({})

prestiti = []

class Libro:
    def __init__(self, titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili

    def info(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}, Anno: {self.anno}, Copie disponibili: {self.copie_disponibili}"


class Utente:
    def __init__(self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente

    def scheda(self):
        return f"Nome: {self.nome}, Età: {self.eta}, ID Utente: {self.id_utente}"

class Prestito:
    def __init__(self, utente=None, libro=None, giorni_prestito=None):
        self.utente = utente
        self.libro = libro
        self.giorni_prestito = giorni_prestito

    def dettagli_prestito(self):
        return f"Utente: {self.utente.scheda()}, Libro: {self.libro.info()}, Giorni prestito: {self.giorni_prestito}"

def presta_libro(utente, libro, giorni):
        if libro.copie_disponibili > 0:
            libro.copie_disponibili -= 1
            titoli_copie[libro.titolo] -= 1
            nuovo_prestito = Prestito(utente, libro, giorni)
            utenti_registrati.add((utente.nome, utente.id_utente))
            prestiti.append(nuovo_prestito)
            return nuovo_prestito
            return 
        else:
            raise ValueError("Libro non disponibile")


prestito1 = presta_libro(Utente("Mario Rossi", 30, 1), Libro("Divina Commedia", "Dante Alighieri", 1320, 1), 7)
prestito2 = presta_libro(Utente("Luigi Bianchi", 25, 2), Libro("Il Nome della Rosa", "Umberto Eco", 1980, 5), 14)
prestito3 = presta_libro(Utente("Giovanni Verdi", 40, 3), Libro("I Promessi Sposi", "Alessandro Manzoni", 1840, 10), 10)
prestito4 = presta_libro(Utente("Maria Neri", 40, 3), Libro("I Promessi Sposi", "Alessandro Manzoni", 1840, 8), 10)
print("Utenti registrati:", utenti_registrati)
print("Titoli e copie:", titoli_copie)
print("Prestiti:", [p.dettagli_prestito() for p in prestiti])
