# Bank Account Management 

class Account: 

    def __init__(self, account_number, balance): 
        self.account_number = account_number 
        self.balance = balance 

class Transaction: 

    def deposit(self, amount): 
        self.balance += amount

    def withdraw(self, amount): 

        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount

class BankAccount(Account, Transaction): 

    def __init__(self, account_number, balance): 
        Account.__init__(self, account_number, balance)

    def display(self):
        print("Account Number:", self.account_number)
        print("Balance: £", self.balance)

account1 = BankAccount(12345678, 7000)

account1.display()

account1.deposit(5000)
account1.withdraw(3000)

account1.display()

account1.withdraw(10000)