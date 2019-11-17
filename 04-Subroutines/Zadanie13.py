def suma(tablica):
    suma = 0
    print("Tablica:", end = ' ')
    for x in tablica:
        print(x, end  = ' ')
        suma += x
    print(f"Suma wartości: {suma}")
tab = [4, 3, 7, 1, 3]
suma(tab)