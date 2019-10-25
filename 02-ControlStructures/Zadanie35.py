a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
delta = b ** 2 - 4 * a * c
if(a == 0 and b == 0):
    print(f"Podane wartości tworzą prostą o wartości {c}")
elif(a == 0):
    x = -c / b
    print(f"Podane wartości tworzą równanie liniowe, z rozwiązaniem równym {x}")
elif(delta > 0):
    x_1 = (-b - delta ** (1/2)) / 2 * a
    x_2 = (-b + delta ** (1/2)) / 2 * a
    print(f"Pierwiastki równania to {x_1} i {x_2}")
elif(delta == 0):
    x = -b / 2 * a
    print(f"Równanie posiada jeden pierwiastek i jest nim {x}")
else:
    print("Równanie nie posiada pierwiastków")
