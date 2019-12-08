from random import randrange

class flight():
    def __init__(self,nmbr):
        self.nmbr = nmbr
        self.altitude = 0
    
    def start(self):
        if self.altitude == 0:
            self.altitude = 1000
        else:
            print("Plane is already in the air")
    
    def alt_change(self,alt):
        self.altitude = alt
        if alt < 300 or alt > 11000:
            print("Dangerous altitude, go back")

    def land(self):
        if self.altitude < 500:
            self.altitude = 0
        else:
            print("Altitude is too high, descend to begin landing")
    
    def status(self):
        print(f"Flight number: {self.nmbr} my altitude is {self.altitude}m")
        
etihad = flight("LOT881")
etihad.start()
etihad.status()
etihad.alt_change(8900)
etihad.status()
etihad.alt_change(200)
etihad.status()
etihad.land()
etihad.status()