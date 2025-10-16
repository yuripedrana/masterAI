
class Libro:
    def __init__(self, titolo, autore, anno, copie):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie = copie

    def __str__(self):
        return f"{self.titolo} di {self.autore} ({self.anno}) - Copie: {self.copie}"
    
class Utente:
    def __init__(self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente

    def __str__(self):
        return f"{self.nome}, Età: {self.eta}, ID: {self.id_utente}"
    
class Prestito:
    def __init__(self, utente, libro, giorni):
            self.utente = utente
            self.libro = libro
            self.giorni = giorni


    def __str__(self):
        return (
                f"Utente: {self.utente}\n"
                f"Libro: {self.libro}\n"
                f"Giorni: {self.giorni}")
    

def Presta_Libro(utente, libro, giorni):
    if libro.copie > 0:
        libro.copie -= 1
        return Prestito(utente, libro, giorni)
    else:
        raise ValueError("Non ci sono copie disponibili per il libro richiesto.")
    
libri = [
    Libro("Trono di Spade", "George R.R. Martin", 1996, 2),
    Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1954, 1),
    Libro("Harry Potter", "J.K. Rowling", 1997, 3),
    Libro("1984", "George Orwell", 1949, 8),
    Libro("Il Piccolo Principe", "Antoine de Saint-Exupéry", 1943, 10)
]

utenti = [
    Utente("Alice", 25, 1),
    Utente("Bob", 30, 2),
    Utente("Charlie", 22, 3)
]
prestiti = []

prestiti.append(Presta_Libro(utenti[1], libri[4], 14))

print("ELENCO LIBRI DISPONIBILI:")
for libro in libri:
    print(libro)

# Stampiamo prestiti
print("\nELENCO PRESTITI:")
for prestito in prestiti:
    print(prestito)
