from random import randrange

class game_cube():
    def __init__(self):
        self.amount = randrange(1,6)
    
    def roll(self):
        self.amount = randrange(1,6)
    
    def show(self):
        print(f"You rolled {self.amount}")

cubes = [game_cube(),game_cube(),game_cube()]
suma = 0

for y in range(3):
    suma = 0
    for x in range(3):
        cubes[x].roll()
        cubes[x].show()
        suma += cubes[x].amount
    print(f"Suma wynosi {suma}")