# wczytanie zmiennych
wzrost = float(input("Podaj wzrost w cm: "))
waga = float(input("Podaj wage w kg: "))
# obliczenie BMI
bmi = waga / ((wzrost/100) * (wzrost/100))
if bmi >= 25:
    print(f"Twoje bmi wynosi {bmi} (nadwaga)")
elif bmi <= 18.5:
    print(f"Twoje bmi wynosi {bmi} (niedowaga)")
else:
    print(f"Twoje bmi wynosi {bmi} (waga prawidłowa)")