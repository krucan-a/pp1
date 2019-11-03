with open('numbers.txt','r') as file:
    lista = [1]
    lista.remove(1)
    for x in file:
        lista.append(x)
lista.sort()
for x in lista:
    print(x, end = ' ')