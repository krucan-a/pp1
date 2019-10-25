pin = "0805"
licznik = 0
while licznik != 3:
    proba = input("Podaj kod PIN: ")
    if proba != pin:
        print("Kod PIN niepoprawny")
        licznik += 1
    else:
        print("Kod PIN poprawny")
        break
if licznik == 3:    
    print("Karta płatnicza zostala zablokowana")
    