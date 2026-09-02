frase = input("Inserisci una frase: ")

frase_invertita = frase[::-1]
palindormo = frase_invertita.replace(" ", "").lower()

print("La frase invertita è:", frase_invertita)
print("La frase è palindormo?:", palindormo)

