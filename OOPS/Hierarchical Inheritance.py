#Hierarchical Inheritance 
#Problem Statement
#Create a program for a Bank System using Hierarchical Inheritance.
#Requirements
#Create a parent class BankAccount
#Attributes:
#account_holder
#balance
#Methods:
#deposit(amount)
#withdraw(amount)
#display_balance()
#Create a child class SavingsAccount that inherits from BankAccount
#Attribute:
#interest_rate
#Method:
#add_interest()
#Create another child class CurrentAccount that inherits from BankAccount
#Attribute:
#overdraft_limit
#Method:
#withdraw_with_overdraft(amount)
#Create one object of SavingsAccount and one object of CurrentAccount and test all methods.

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
       

class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
        else:
            print("Overdraft limit exceeded!")

savings = SavingsAccount("riya", 10000, 5)
savings.display_balance()
savings.deposit(2000)
savings.withdraw(3000)
savings.add_interest()
savings.display_balance()
print("\n")

current = CurrentAccount("Ramya", 5000, 2000)
current.display_balance()
current.deposit(1000)
current.withdraw(4000)
current.withdraw_with_overdraft(3000)
current.display_balance()
