# wczytanie zmiennych i biblioteki math
import math
x = float(input("Podaj boki trójkąta :"))
y = float(input())
z = float(input())
# obliczanie pola i połowy obwodu
pol_obw = 0.5 * (x + y + z)
pole_heron = math.sqrt(pol_obw * (pol_obw - x) * (pol_obw - y) * (pol_obw - z))
print(f"Pole trójkąta wynosi {pole_heron}")
