import csv
class GestoreLibri:
    def __init__(self):
        self.file_name = "libri.csv"

    def lettura(self):
        try:
            with open(self.file_name, "r") as file:
                return list(csv.DictReader(file))
        except FileNotFoundError:
            print("Il file non esiste.")
            return []

    def stampa(self):
        libri = self.lettura()
        for libro in libri:
            print("Titolo:", libro["titolo"], "Autore:", libro["autore"], "Anno:", libro["anno"])
      

    def SoloLibriHarryPotter(self):
        try:
            libri = self.lettura()
            for libro in libri:
                if "B.A" in libro["autore"]:
                    print("Titolo:", libro["titolo"], "Autore:", libro["autore"], "Anno:", libro["anno"])
        except KeyError:
            print("Errore: il file CSV non contiene la colonna 'autore'.")

print("Libri Harry Potter:")
gestore = GestoreLibri()
gestore.SoloLibriHarryPotter()
print("Tutti i libri:")
gestore.stampa()