liczby = [32, 16, 5, 8, 24, 7]
with open('Zadanie13.txt','wa') as file:
    for x in liczby:
        file.write(f'{str(x)}\n')

