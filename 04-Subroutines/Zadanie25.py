def jestImie(imie,imiona):
    if imie in imiona:
        return True
    else:
        return False
imiona = ["Janek","Ania","Wojtek","Zosia"]
imie = ["Wojtek"]
if jestImie(imie,imiona):
    print("Imię zawarte jest w wykazie imion")