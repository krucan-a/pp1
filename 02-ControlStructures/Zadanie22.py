tab = [15, 8, 31, 47, 2, 19]
suma = 0
ilosc = 0
for n in tab:
    if(n % 2 == 1):
        suma += n
        ilosc += 1
print(f"Szukana średnia to {suma/ilosc}")