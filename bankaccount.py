
class bankAccount:
    accounts={}
    def __init__(self,name):
        self.name=name
        bankAccount.accounts[self.name]=0
    def deposit(self, amount):
        bankAccount.accounts[self.name]+=amount
        print(f'the account: {self.name} has been debited with ${amount}')
    def withdraw(self, amount):
        bankAccount.accounts[self.name]-=amount
        print(f'the account: {self.name} has been credited with ${amount}')
    def transfer(self, reciever, amount):
        self.withdraw(amount)
        reciever.deposit(amount)
account1=bankAccount('jazmin')
account2=bankAccount('rabat')
account3=bankAccount('marshal')

account1.deposit(9000)
account2.deposit(10000)
account3.deposit(7000)
print(bankAccount.accounts,"\n")

account1.withdraw(500)
account2.withdraw(600)
account3.withdraw(700)
print(bankAccount.accounts,"\n")

account1.transfer(account2, 500)
account1.transfer(account3, 700)
print(bankAccount.accounts)
