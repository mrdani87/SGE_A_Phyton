num = [1, 4, 5, 67, 34, 55, 78, 90, 2, 44, 65, 33, 35, 50]

parells = []
imparells = []

for n in num:
    if n % 2 == 0:
        parells.append(n)
    else:
        imparells.append(n)

print(f"Números parells: {parells}")
print(f"Números imparells: {imparells}")
