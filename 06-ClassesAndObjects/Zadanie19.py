class bank_acc():
    def __init__(self,acc_nmbr):
        self.nmbr = acc_nmbr
        self.balance = 0
    
    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds on account")
        else:
            self.balance -= amount

    def status(self):
        print(f"Account number: {self.nmbr}")
        print(f"Balance: {self.balance}$")

    
acc = bank_acc("12 3456 5555 9090 1111 0000 7722")
acc.status()
acc.deposit(25.30)
acc.status()
acc.withdraw(31.70)
acc.status()
acc.withdraw(14)
acc.status()
