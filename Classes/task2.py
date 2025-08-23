# Task: Create a class called BankAccount with:

# Attributes: account_number, account_holder, balance (default 0)

# Methods:

# deposit(amount)

# withdraw(amount)

# display_balance()

# Practice:

# Create an object and simulate some deposits and withdrawals.

class BankAccount:
    def __init__(self, account_number:int, account_holder, balance=0):
        if not isinstance(account_number, int):
            raise TypeError("Account number must be an integer")
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}!!")
    
    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
            print(f"Amount Withdrawn is {amount}")
        else:
            print("INSUFFICIENT BALANCE!! Can't withdraw!")
        
    def display_balance(self):
        print(f"Hi {self.account_holder}! Your account balance is {self.balance}")
        


user1 = BankAccount('abcd2123', 'Rudra', 10000)
print(user1.account_number)
user1.deposit(5000)
user1.display_balance()
user1.withdraw(2000)
user1.display_balance()
user1.withdraw(20000)