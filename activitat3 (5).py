num = [1, 4, 5, 67, 34, 55, 78, 90, 2, 44, 65, 33, 35, 50]

suma_parells = 0
suma_imparells = 0

for n in num:
    if n % 2 == 0:
        suma_parells += n
    else:
        suma_imparells += n

print(f"La suma dels números parells és: {suma_parells}")
print(f"La suma dels números imparells és: {suma_imparells}")
