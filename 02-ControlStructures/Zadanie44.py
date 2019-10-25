limit = int(input("Podaj limit prędkości (km/h): "))
predkosc = int(input("Podaj prędkość pojazdu (km/h): "))
roznica = predkosc - limit
if(roznica < 0):
    print("Mandat (zł): 0")
elif(roznica > 10):
    print(f"Mandat (zł): {50 + 15 * (roznica - 10)}")
else:
    print(f"Mandat (zł): {roznica * 5}")