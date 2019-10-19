# wczytanie zmiennych i importowanie biblioteki math
x = int(input("Podaj x: "))
y = int(input("Podaj y: "))
import math
print(f"Najwiekszy wspolny dzielnik liczb {x} i {y} to {math.gcd(x,y)}")