class Sala():
    def __init__(self, nazwa, liczbaMiejsc):
        self.nazwa = nazwa
        self.liczbaMiejsc = liczbaMiejsc
    
class Sale(Sala):
    def __init__(self):
        self.sale = []
    
    def dodaj(self, Sala):
        self.sale.append(Sala)
    
    def liczba_sal(self):
        return len(self.sale)
    
    def razem_miejsc(self):
        suma = 0
        for x in self.sale:
            suma += x.liczbaMiejsc
        return suma
    
    def liczba_miejsc(self, nazwaSali):
        for x in self.sale:
            if x.nazwa == nazwaSali:
                return x.liczbaMiejsc
    
    def liczbaSalPrzedzial(self,od, do):
        sum = 0
        for x in self.sale:
            if x.liczbaMiejsc >= od and x.liczbaMiejsc <= do:
                sum += 1
        return sum

uek = Sale()
ajti = Sala("IT",200)
socjo = Sala("Socjo", 300)
eko = Sala("eko",500)
uek.dodaj(ajti)
uek.dodaj(socjo)
uek.dodaj(eko)
print(uek.liczba_sal())
print(uek.razem_miejsc())
print(uek.liczba_miejsc("Socjo"))
print(uek.liczbaSalPrzedzial(100,400))
