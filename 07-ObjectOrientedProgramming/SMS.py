from message import Message

class SMS(Message):
    def __init__(self, nmbrSender, nmbrReceiver, content):
        super().set_message(content)
        self.nmbrSender = nmbrSender
        self.nmbrReceiver = nmbrReceiver 
    def sendSMS(self):
        print("Wysyłanie SMS")
        print("Wysyłanie SMS...")
        print(f"Od: {self.nmbrSender}")
        print(f"Do: {self.nmbrReceiver}")
        print(f"Treść: {self.message}")