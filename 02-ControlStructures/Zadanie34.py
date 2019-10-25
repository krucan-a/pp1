import datetime
now = datetime.datetime.now()
PESEL = input("Podaj swój pesel: ")
# sprawdzenie w którym wieku została urodzona osoba
data_spr = int(PESEL[2:4])
if data_spr < 12:
    data_urodzenia = int(PESEL[0:2]) + 1900
elif data_spr > 40:
    data_urodzenia = int(PESEL[0:2]) + 1800
else:
    data_urodzenia = int(PESEL[0:2]) + 2000
# obliczenie wieku
wiek = now.year - data_urodzenia
# ustalanie płci
if (int(PESEL[9])% 2 == 1):
    plec = "mężczyzna"
else:
    plec = "kobieta"
print(f"Płeć: {plec}")
print(f"Wiek: {wiek}")    