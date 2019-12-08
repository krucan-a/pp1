# odczytaj współczynniki z klawiatury, zwraca tablicę współczynników
import math
def czytajWspolczynniki(wspolczynniki):
    wspolczynniki[0] = float(input("Podaj a: "))
    wspolczynniki[1] = float(input("Podaj b: "))
    wspolczynniki[2] = float(input("Podaj c: "))
# oblicz deltę
def obliczDelte(wspolczynniki):
    return float(wspolczynniki[1]^2 - 4 * wspolczynniki[0] * wspolczynniki[2])
# wyznacz pierwiastki równania - zwraca tablicę pierwiastków (jeden lub dwa elementy) lub pustą tablicę, jeśli delta < 0
def obliczPierwiastki(wspolczynniki):
    delta = obliczDelte(wspolczynniki)
    if delta < 0:
        x = []
        return x
    elif delta == 0:
        x1 = (wspolczynniki[1] * -1 /(2 * wspolczynniki[0]))
        x = [x1]
        return x
    else:
        x1 = (wspolczynniki[1] * -1 + math.sqrt(delta) /(2 * wspolczynniki[0]))
        x2 = (wspolczynniki[1] * -1 - math.sqrt(delta) /(2 * wspolczynniki[0]))
        x = [x1,x2]
        return x
# wyświetl wyznaczone pierwiastki równania kwadratowego
def wyswietlPierwiastki(wspolczynniki):
    x = obliczPierwiastki(wspolczynniki)
    if len(x) == 0:
        print("Pierwiastki równania: brak")
    if len(x) == 1:
        print(f"Pierwiastki równania: x1={x[0]}")
    if len(x) == 2:
        print(f"Pierwiastki równania: x1={x[0]} x2={x[1]}")