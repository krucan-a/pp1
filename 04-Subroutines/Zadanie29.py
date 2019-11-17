import math
tab = [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]
def mediana(tab):
    tab.sort()
    for x in tab:
        print(x,end = " ")
    if(len(tab) % 2 == 0):
        x = (tab[int(len(tab)/2) + 1] + tab[int(len(tab)/2) - 1]) / 2
        return x
    else:
        index = int(math.ceil(len(tab)/2))
        return tab[index]
def dominanta(tab):
    counter = 0
    num = tab[0]
    for x in tab:
        amount = tab.count(x)
        if(amount > counter):
            counter = amount
            num = x
    return num
print(f"Mediana to {mediana(tab)}, dominanta to {dominanta(tab)}")