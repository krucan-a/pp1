from message import Message

class EMail(Message):
    def __init__(self, nadawca, odbiorca, temat):
        super().__init__()
        self.nadawca = nadawca
        self.odbiorca = odbiorca
        self.temat = temat
    def send(self):
        print("Wysyłanie maila...")
        print(f"Od: {self.nadawca}")
        print(f"Do: {self.odbiorca}")
        print(f"Temat: {self.temat}")
        print(f"Treść: {self.message}")