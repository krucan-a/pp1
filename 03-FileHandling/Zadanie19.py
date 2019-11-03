with open('universities.txt','r') as file_read:
    lista = ["1"]
    lista.remove("1")
    for x in file_read:
        lista.append(x)
lista.sort()
with open('Zadanie19.txt','w') as file_write:
    for x in lista:
        file_write.write(f"{x}")