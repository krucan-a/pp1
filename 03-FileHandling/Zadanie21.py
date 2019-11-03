suma = ilosc = 0
with open('numbers.txt','r') as file_r:
    for x in file_r:
        if(x[2] == ','):
            x_split = x.split(',')
            for y in x_split:
                ilosc += 1
                suma += int(y)
        else:
            ilosc += 1
            suma += int(x)
print(f"Suma wynosi {suma}, ilosc liczb wynosi {ilosc}")
