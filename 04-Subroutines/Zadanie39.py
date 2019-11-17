def nmbr_in_range(nmbr, x, y):
    if nmbr >= x and nmbr <= y or nmbr <= x and nmbr >= y:
        return True
    else:
        return False

nmbr = int(input("Podaj liczbę: "))
x = int(input("Podaj początek zakresu: "))
y = int(input("Podaj koniec zakresu: "))
if nmbr_in_range(nmbr, x, y):
    print("LIczba znajduje się w tym przedziale domkniętym")
else:
    print("LIczba nie znajduje się w tym przedziale domkniętym")