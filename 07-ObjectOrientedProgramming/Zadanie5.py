class Track():
    def __init__(self, name, artist, album, year):
        self.name = name
        self.artist = artist
        self.album = album
        self.year = year

    def __str__(self):
        return "Wykonawca: " + self.artist + "\nUtwór: "+ self.name +"\nAlbum: " + self.album + "\nRok: " + str(self.year)

mySong = Track("Dawid Podsiadło", "Nie ma fal", "Małomiasteczkowy", 2018)
print(mySong)