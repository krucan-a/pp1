liczba = int(input("Podaj liczbę: "))
suma = srednia = 0
ilosc = 0
while(liczba != 0):
    ilosc += 1
    suma += liczba
    srednia = suma / ilosc
    liczba = int(input("Podaj liczbę: "))
print(f"REZULTAT: Liczb={ilosc}, Suma={suma}, Średnia={srednia}")