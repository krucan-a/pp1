def transpozycja(macierz):
    j = 0
    for i in range(len(macierz)):
        while j < len(macierz[0]):
            macierz[i][j], macierz[j][i] = macierz[j][i], macierz[i][j]
            j += 1
        j = i + 1
    return macierz
macierz = [ [1, 2, 0, 2],
            [0, 0, 3, 3],
            [5, 1, 1, 4],
            [3, 4, 2, 8]]
macierz_transponowana = transpozycja(macierz)
for r in macierz_transponowana:
    for c in r:
        print(c, end = ' ')
    print()