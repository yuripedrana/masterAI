class Divisione:
    def dividi(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Errore: divisione per zero non consentita"

class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

        if eta < 0:
            raise ValueError("L'età non può essere negativa")

        self.nome = nome
        self.eta = eta


    def __str__(self):
        return f"Nome: {self.nome}, Età: {self.eta}"


class Banca:
    def preleva(self, conto, saldo):
        if conto < saldo:
            raise ValueError("Fondi insufficienti")
        return conto - saldo

print(Divisione().dividi(10, 2))
print(Persona("Mario", 30))
print(Banca().preleva(10, 50))
