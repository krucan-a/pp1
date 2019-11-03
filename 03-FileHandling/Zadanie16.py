from statistics import mean
import re
komunikat = 'wtorek - 23C, środa - 17C, czwartek 25C'
cyfry = re.findall('\d{2}',komunikat)
suma = 0
for x in cyfry:
    suma += int(x)
srednia = suma / len(cyfry)
print(f"Średnia temperatur wynosi {(round(srednia, 2))}")
