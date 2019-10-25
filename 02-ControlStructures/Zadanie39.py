pierwszy_wyraz = 0
drugi_wyraz = 1
print(pierwszy_wyraz, end=" ")
print(drugi_wyraz, end=" ")
for x in range(1,50):
    pomocnicza = drugi_wyraz
    drugi_wyraz = pierwszy_wyraz + drugi_wyraz
    print(drugi_wyraz, end=" ")
    pierwszy_wyraz = pomocnicza
    