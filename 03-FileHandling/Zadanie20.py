with open('numbers.txt','r') as file_r:
    lista = [1]
    lista.remove(1)
    for x in file_r:
        lista.append(x)
with open('evennumbers.txt','w') as file_w:
    for x in lista:
        if(int(x) % 2 == 0):
            file_w.write(x)