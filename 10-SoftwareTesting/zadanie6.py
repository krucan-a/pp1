from random import randrange

class Macierz():
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.macierz = []
    
    def Create(self):
        for x in range(self.m):
            tab = []
            for y in range(self.n):
                tab.append(randrange(0,9))
                if y == self.n-1:
                    self.macierz.append(tab)

    
    def Draw(self):
        for x in range(self.m):
            for y in range(self.n):
                print(self.macierz[x][y], end = " ")
            print("")
    
    def __add__(self, other):
        macierz = []
        tab = []
        if self.m == other.m and self.n == other.n:
            for x in range(self.m):
                tab = []
                for y in range(self.n):
                    tab.append(self.macierz[x][y] + other.macierz[x][y])
                    if y == self.n-1:
                        macierz.append(tab)
        return macierz
                    
macierz1 = Macierz(3,4)
macierz1.Create()
macierz1.Draw()
print("")
macierz2 = Macierz(3,4)
macierz2.Create()
macierz2.Draw()
print("")
macierz3 = Macierz(3,4)
macierz3.macierz = macierz1 + macierz2
macierz3.Draw()