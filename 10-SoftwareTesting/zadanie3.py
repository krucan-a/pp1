class Prostokat():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def surface(self):
        return self.a * self.b
    
    def __add__(self,other):
        return self.surface() + other.surface()

lul = Prostokat(5,5)
print(lul + lul)