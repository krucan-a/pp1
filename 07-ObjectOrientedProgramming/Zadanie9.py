class Message():
    def __init__(self):
        self.message = ''
    def set_message(self,message):
        self.message = str.upper(self.message[0]) + self.message[0:] + " BYE"
