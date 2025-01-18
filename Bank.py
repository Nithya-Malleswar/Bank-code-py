class bank:
    def __init__(self,accholder,accno,accbal,acctype):
        self.accholder=accholder
        self._accno=accno
        self.__accbal=accbal
        self.acctype=acctype
    def deposit(self,Amount):
        if Amount > 0:
            self.__accbal += Amount
            print(f"The deposit amount is {Amount} and current balance is {self.__accbal}")
        else:
            print("Insufficient funds")
    def withdraw(self,Amount):
        if Amount > 0 and Amount <= self.__accbal:
            self.__accbal -= Amount
            print(f"The withdraw amount is {Amount} and current balance is {self.__accbal}")
        else:
            print("Insufficient Funds")
    def TotalAmount(self):
        print(f"The current bank balance is {self.__accbal:.2f}")

bank1=bank("Nithya",300030001615,5000,"savings")
bank1.deposit(5000)
bank1.withdraw(2000)
bank1.TotalAmount()
