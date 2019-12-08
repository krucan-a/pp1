from math import gcd

class fraction():
    def __init__(self,numerator,denominator):
        self.numerator = int(numerator)
        self.denominator = int(denominator)
    
    def ease(self):
        numerator = self.numerator
        denominator = self.denominator
        self.numerator = int(self.numerator/gcd(self.numerator,self.denominator))
        self.denominator = int(self.denominator/gcd(numerator,denominator))

    def show(self):
        print(f"{self.numerator}/{self.denominator}")

adin = fraction(1,3)
dwa = fraction(4,8)
dwa.ease()
adin.show()
dwa.show()