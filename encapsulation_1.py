# Bank Account Manager 

class BankAccount: 
    def __init__(self, account_holder, balance, pin): 

        self.account_holder = account_holder

        # Protected

        self._accountNum = "ACC12345"

        # Private

        self.__balance = balance 
        self.__pin = pin

    def deposit(self, amount): 

        if amount > 0:
            self.__balance += amount 
            print("£", amount, "deposited successfully.")

        else: 
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount): 

        if amount <= 0: 
            print("Withdrawl amount must be greater than 0.")

        elif amount > self.__balance: 
            print("Insufficient balance.")

        else: 
            self.__balance -= amount 
            print("£", amount, "withdrawn successfully.")

    # Return current balance

    def get_balance(self):
        return self.__balance

    # Change PIN

    