ilosc = int(input("Podaj ilosc liczb: "))
x = 2
spr = 0
if(ilosc < 3):
    print("Liczby pierwsze: 2 3 5")
else:
    x = 3
    print("Liczby pierwsze: 2", end = " ")
    while ilosc - 1 > 0: 
        y = 2
        while (y <= x ** (1/2)):
            if( x % y == 0):
                spr = 1
                y = x
            else:
                y += 1
        if spr == 0:
            print(x,end = " ")
            spr = 0
            x += 2
            ilosc -= 1
        else:
            x += 2
            spr = 0