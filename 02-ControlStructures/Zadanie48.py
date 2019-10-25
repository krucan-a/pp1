import random
liczby = [None] * 49
i = 0
while i < 49:
    liczby[i] = i + 1
    i += 1
x = 0
random.shuffle(liczby)
while x < 49:
    if(liczby[x] < 10):
        print(liczby[x], end = "  ")
    else:
        print(liczby[x],end =" ")
    x += 1
    if(x % 7 == 0):
        print("\n")
