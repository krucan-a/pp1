class student():
    nrAlbumuStartowy = 99999

    def __init__(self, imie, nazwisko, kierunekStudiow):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nrAlbumu = student.nrAlbumuStartowy + 1
        student.nrAlbumuStartowy += 1
        self.kierunekStudiow = kierunekStudiow
    
    def __str__(self):
        return self.imie + " " + str.upper(self.nazwisko) + f"({self.nrAlbumu}), " + self.kierunekStudiow + ", UEK Krakow"

andrzej = student("Andrzej", "Nowak", "Informatyka Stosowana")
mariusz = student("Mariusz", "Nowak", "Informatyka Stosowana")
janusz = student("Janusz", "Nowak", "Informatyka Stosowana")

print (andrzej, mariusz, janusz)