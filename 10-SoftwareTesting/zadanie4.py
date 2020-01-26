class Zbiory():
    @staticmethod
    def iloczyn(zbior1, zbior2):
        iloczynZbiorow = []
        for x in zbior1:
            if x in zbior2:
                if x not in iloczynZbiorow:
                    iloczynZbiorow.append(x)
        return iloczynZbiorow
    @staticmethod
    def suma(zbior1, zbior2):
        sumaZbiorow = []
        for x in zbior1:
            if x not in sumaZbiorow:
                 sumaZbiorow.append(x)
        for x in zbior2:
            if x not in sumaZbiorow:
                sumaZbiorow.append(x)
        return sumaZbiorow
    @staticmethod
    def roznica(zbior1, zbior2):
        roznicaZbiorow = []
        for x in zbior1:
            if x in zbior2:
                if x not in roznicaZbiorow:
                     roznicaZbiorow.append(x)
        return roznicaZbiorow

Zbior1 = [1,2,3,4]
Zbior2 = [3,4,5,6]
print(Zbiory.iloczyn(Zbior1,Zbior2))
print(Zbiory.suma(Zbior2,Zbior1))
print(Zbiory.roznica(Zbior2,Zbior1))
print(Zbiory.roznica(Zbior1,Zbior2))