import random
def rzucKostka():
    return random.randrange(1,7)

suma = 0
print("Wyrzucone oczka:",end = " ")
for x in range(3):
    y = rzucKostka()
    suma += y
    print(y,end = ' ')
print(f"Suma oczek: {suma}")