def array_singular_values(tab):
    tab.sort()
    singular_values = []
    for i in range(len(tab)):
        if i == 0:
            singular_values.append(tab[i])
        elif tab[i] != tab[i-1]:
            singular_values.append(tab[i])
    return singular_values
tab = [1,1,1,1,2,3,3,3,5,3,5,6,3]
tab_singular_values = array_singular_values(tab)
for x in tab_singular_values:
    print(x, end=" ")