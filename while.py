numero_utente = int(input("Inserisci un numero positivo: "))

while numero_utente < 0:
    numero_utente = int(input("Per favore, inserisci un numero positivo: "))

print("Hai inserito un numero positivo:", numero_utente)


numero = 25
somma_cifre = 0

while numero > 0:
    somma_cifre += numero % 10
    numero //= 10

print("La somma delle cifre è:", somma_cifre)
