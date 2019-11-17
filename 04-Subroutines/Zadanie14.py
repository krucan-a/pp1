def wystepuje(liczba, tablica):
    if(liczba in tablica):
        print("Podana liczba występuje w tablicy")
liczba = int(input("Liczba: "))
tablica = input("Tablica: ")
tablica = tablica.split(" ")
tablica = [int(i) for i in tablica]
wystepuje(liczba,tablica)