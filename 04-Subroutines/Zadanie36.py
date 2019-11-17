def sum_el_tab(tab):
    sum = 0
    for x in tab:
        if isinstance(x, int):
            sum += x
        else:
            sum += sum_el_tab(x)
    return sum
tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]
print(sum_el_tab(tab))