wzrost = int(input("Proszę podać swój wzrost w cm: "))
waga = float(input("Proszę podać swoją wagę w kg: "))
assert wzrost < 220 and wzrost > 150, "Obsługiwany wzrost to 150 cm do 220 cm"
assert waga < 150.0 and waga > 40.0, "Obsługiwana waga to od 40 kg do 150 kg"
bmi = waga / (wzrost/100) ** 2
print(f"Twoje BMI wynosi {bmi}")