import numpy as np

dati = np.random.randint(10,100, size=(6,5))

print("dati originali:\n", dati)

print("dati shape:\n", dati.shape)
print("dati dtype:\n", dati.dtype)

print("\nPrima Riga:\n", dati[0])
print("\n Prima Colonna:\n", dati[:,0])
print("\n Submatrice: (prime 2 righe e prime 3 colonne)\n", dati[:2,:3])

view = dati[:2,:2]
copy = dati[:2,:2].copy()

view[0-0] = 999
print("\nView modificata:\n", view)
print("\nDati originali dopo modifica della view:\n", dati)
print("\nCopy prima della modifica:\n", copy)

reshaped = dati.reshape(3,10)
print("\nDati reshaped (3 righe, 10 colonne):\n", reshaped)

print("iterazione sugli elementi di dati:",)
for x in np.nditer(dati):
    print(int(x), end=" ")

print()

extra = np.random.randint(10,100, size=(6,2))

unito = np.hstack((dati, extra))
print("\nDati uniti (orizzontalmente):\n", unito)

split = np.split(unito, 2)

print("\nDati divisi in 2 parti:\n", split[0], split[1])

mask = dati > 50
print("\ndati maggiori di 50):\n", mask)

ordinati = np.sort(dati, axis=1)
print("\nDati ordinati:\n", ordinati)


radici = np.sqrt(dati)
print("\nRadici quadrate dei dati:\n", radici)

