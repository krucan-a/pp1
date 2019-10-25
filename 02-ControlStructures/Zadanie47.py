kwota = int(input("Podaj kwotę w zł: "))
print(f"5 zł - {int((kwota - (kwota % 5)) / 5)} szt")
print(f"2 zł - {int((kwota % 5 - (kwota % 5)% 2) / 2)} szt")
print(f"1 zł - {(kwota % 5) % 2} szt")