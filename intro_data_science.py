import pandas as pd
import matplotlib.pyplot as plt

dati = {"Settimana": [1,2,3,4,5,6],
        "Vendite": [250,300,450,350,450,600]}

df = pd.DataFrame(dati)

media_vendite = df["Vendite"].mean()

print("Media vendite", media_vendite)



settimana_max_vendite = df.loc[df["Vendite"].idxmax(), "Settimana"]
print("La settimana con più vendite è la", settimana_max_vendite)

fig, ax = plt.subplots(1, 1)
ax.bar(df["Settimana"], df["Vendite"], color=["red" if v < media_vendite else "green" for v in df["Vendite"]])

ax.axhline(media_vendite, color="red", linestyle="--", label="Media")
ax.set_xlabel("Settimana")
ax.set_ylabel("Vendite")
ax.set_title("Vendite Settimanali")
ax.legend()
ax.plot(df["Settimana"], df["Vendite"], marker="o", color="skyblue")
ax.axhline(media_vendite, color="red", linestyle="--", label="Media")
ax.set_xlabel("Settimana")
ax.set_ylabel("Vendite")
ax.set_title("Vendite Settimanali")
ax.legend()
plt.show()



