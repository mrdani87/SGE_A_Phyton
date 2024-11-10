nota = float(input("Introdueix nota: "))

if 0 <= nota < 5:
    resultat = "L’alumne ha suspès."
elif 5 <= nota <= 6.5:
    resultat = "L’alumne ha aprovat."
elif 6.6 <= nota <= 8:
    resultat = "L’alumne té un notable."
elif nota > 8:
    resultat = "L’alumne té un excel·lent."
else:
    resultat = "Nota no vàlida."

print(resultat)
