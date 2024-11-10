salari = float(input("Salari: ")) 

if salari < 15000:
    iva = 0
elif salari < 30000:
    iva = 10
elif salari < 60000:
    iva = 21
else:
    iva = 0 

iva_calculat = salari * iva / 100

print(f"Salari: {salari} €")
print(f"IVA aplicat: {iva}%")
print(f"Import de l'IVA: {iva_calculat} €")