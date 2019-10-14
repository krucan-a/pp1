'''
Obliczanie pola powierzchni i obwodu koła o zadanym promieniu
'''
#ustal promień koła i PI
promien_kola = 5
import math
pi = math.pi
#oblicz pole i obwód
pole = pi * promien_kola ** 2
obwod = 2 * pi * promien_kola
#wyswietl rezultaty
print(f"Pole kola o promieniu {promien_kola} wynosi {pole}")
print(f"Obwod kola o promieniu {promien_kola} wynosi {obwod}")