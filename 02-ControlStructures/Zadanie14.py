wiek_ludzki = int(input("Podaj wiek psa w ludzkich latach: "))
if wiek_ludzki <= 2:
    wiek_psa = wiek_ludzki * 10.5
else:
    wiek_psa = 21 + 4 * (wiek_ludzki - 2)
print(f"Wiek psa w psich latach to {wiek_psa} lata")