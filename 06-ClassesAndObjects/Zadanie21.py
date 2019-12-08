class Statystyka():
    def __init__(self):
        self.nmbrs = []
    
    def add(self,nmbr):
        self.nmbrs.append(nmbr)

    def show(self):
        for x in self.nmbrs:
            print(x,end = " ")
    
    def biggest(self):
        nmbrs_2 = self.nmbrs
        nmbrs_2.sort()
        print(nmbrs_2[0])
    
    def smallest(self):
        nmbrs_2 = self.nmbrs
        nmbrs_2.sort(False)
        print(nmbrs_2[0])
    
    def average(self):
        suma = 0
        for x in self.nmbrs:
            suma += x
        print(suma/len(self.nmbrs))
    
    def median(self):
        