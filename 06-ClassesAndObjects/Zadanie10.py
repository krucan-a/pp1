class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0

    def on(self):
        self.is_on = True

    def off(self):
        self.is_on = False
    
    def vol_up(self):
        if self.volume < 10:
            self.volume += 1

    def vol_down(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self,channels_list):
        self.channels = channels_list

    def show_channels(self):
        if self.channels == []:
            print("BRAK KANAŁÓW")
        else:
            print("LISTA KANAŁÓW TV")
            for x in range(len(self.channels)):
                print(f"{x+1}. {self.channels[x]}")

    def show_status(self):
        if self.is_on and len(self.channels)>self.channel_no-1:
            print(f"Telewizor jest włączony, kanał {self.channel_no} ({self.channels[self.channel_no-1]}), głośność {self.volume}")
        elif self.is_on:
            print(f"Telewizor jest załączony, głośność {self.volume}")
        else:
            print("Telewizor jest wyłączony")

channels = ["TVP1","TVP2","Polsat","TVN","Filmbox","Canal+","HBO"]

Manta = TV()
Manta.show_status()
Manta.on()
Manta.show_status()
Manta.vol_up()
Manta.show_status()
Manta.vol_down()
Manta.show_status()
Manta.show_channels()
Manta.set_channels(channels)
Manta.show_channels()
Manta.set_channel(7)
Manta.show_status()
Manta.off()
Manta.show_status()