liczba = int(input("Podaj liczbę: "))
liczba_bin = str(liczba % 2)
liczba = liczba // 2
while liczba > 0:
    liczba_bin = liczba_bin + str(liczba % 2)
    liczba = liczba // 2
print(liczba_bin[::-1])