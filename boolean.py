eta = int(input("Inserisci la tua età: "))
hai_la_patente = (str(input("Hai la patente? (si/no): ")))
puo_guidare = eta >= 18 and hai_la_patente == "si"
print("Puoi guidare?:", puo_guidare)

in_ritardo = False
abbonamento_premium = True
puo_entrare_in_biblioteca = in_ritardo or abbonamento_premium
print("Puoi entrare in biblioteca?:", puo_entrare_in_biblioteca)

