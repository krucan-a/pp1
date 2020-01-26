class Stos():
    def __init__(self):
        self.stosKart = []
        self.iloscKart = 0

    def wstaw(self,nazwa_karty):
        self.stosKart.append(nazwa_karty)
        self.iloscKart += 1
    
    def zdejmij(self):
        print(f"Karta {self.stosKart[self.iloscKart-1]} została zdjęta ze stosu")
        self.stosKart.pop()
        self.iloscKart -= 1
    
    def jest_pusty(self):
        if self.iloscKart == 0:
            return "Stos jest pusty"
        else:
            return "Stos jest niepusty"

talia = Stos()
talia.wstaw("król")
talia.wstaw("dama")
talia.wstaw("10")
talia.wstaw("3")
talia.zdejmij()
talia.zdejmij()
talia.zdejmij()
print(talia.jest_pusty())
talia.zdejmij()
print(talia.jest_pusty())