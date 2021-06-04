class Account:
    def __init__(self,accountNumber,phoneNumber,name,loan_limit):
        self.accountNumber=accountNumber
        self.phoneNumber=phoneNumber
        self.name=name
        self.loan=0
        self.balance=0
        self.loan_limit=loan_limit
    def deposit(self,amount):
        if amount<=0:
            return f"The amount must be greater than zero"
        else:
            self.balance+=amount
            return f"Dear {self.name} you have deposited {amount} your balance is {self.balance}"
    def show(self,balance):
            return self.balance

    def withDraw(self,amount):
        if amount<0:
            return "You can't withdraw negative amount "
        elif amount>self.balance:
            return "You can have insufficient balance"
        else:
             self.balance-=amount
             return f"You have successfully withdrawn {amount} your balance is {self.balance}"
    def borrow(self,amount):
        if amount>=self.loan_limit:
            return f"You cant borrow"
        elif self.loan>0:
            return f"You already have an existing loan"
        else:
            self.loan+=1
            self.balance+=amount
            return "You have successfully borrowed"

