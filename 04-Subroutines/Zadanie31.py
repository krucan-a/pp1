def reverse(tab):
    tab_reversed = [tab[len(tab)-1]]
    for x in range(len(tab)-1, 0, -1):
        tab_reversed.append(tab[x-1])
    return tab_reversed
tab = [2, 5, 4, 1, 8, 7, 4, 0, 9]
for x in tab:
    print(x, end = " ")
print("")
for x in reverse(tab):
    print(x, end = " ")

