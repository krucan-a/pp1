x = int(input("Podaj wartość x: "))
y = int(input("Podaj wartość y: "))
if(x < 0 or y < 0):
    print(f"Jedna z wartości {x} lub {y} jest ujemna")
else:
    print(f"Obydwie wartości {x} oraz {y} są nieujemne")
    