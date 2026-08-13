# oop2

class BankAccount: 

    def __init__(self, holder, balance): 
        self.holder = holder
        self.balance = balance

    def deposit(self, amount): 
        self.balance += amount 
        print(amount, "deposited successfully.")

    def withdraw(self, amount): 
        if amount <= self.balance: 
            self.balance -= amount 
            print(amount, "withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display(self):
        print("\nAccount Holder:", self.holder)
        print("Balance:", self.balance)

acc1 = BankAccount("John", 10000)

acc1.display()
acc1.deposit(3000)
acc1.display()
acc1.withdraw(5000)
acc1.display()