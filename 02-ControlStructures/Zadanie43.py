liczby = [1,1,1]
liczby[0] = int(input("Podaj pierwszą liczbę: "))
liczby[1] = int(input("Podaj drugą liczbę: "))
liczby[2] = int(input("Podaj trzecią liczbę: "))
liczby.sort()
print("Liczby w kolejności rosnącej:",end=" ")
for x in liczby:
    print(x,end=" ")