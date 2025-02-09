class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f"Account {name} has just created with ${balance:.2f} balance.")


    def getBalance(self):
        print(f"Account {self.name} has balance of ${self.balance:.2f}")

    
    def viableTransaction(self, amount):
        if self.balance < amount:
            raise BalanceException(f"Insuffient balance, current balance: ${self.balance:.2f}")
        

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print(f"Account {self.name} has withdrawn ${amount:.2f}. Remaining balance is ${self.balance:.2f}")
        except BalanceException as e:
            print(str(e))


    def deposit(self, amount):
        self.balance += amount
        print(f"Account {self.name} has deposited ${amount:.2f}. New balance is ${self.balance:.2f}")


    def transfer(self, account, amount):
        try:
            self.viableTransaction(amount)
            print("**** Transfer Start ****")
            self.balance -= amount
            print(f"Account {self.name} has withdrawn ${amount:.2f}. Remaining balance is ${self.balance:.2f}")
            account.deposit(amount)
            print(f"Transfer successful from account {self.name} to account {account.name} with amount ${amount:.2f}")
            print("**** Transfer End ****")
        except BalanceException as e:
            print(str(e))


class InterestRewards(BankAccount):
    def deposit(self, amount):
        self.balance += amount + (amount * .01)
        print(f"Account {self.name} has deposited ${amount:.2f}. New balance is ${self.balance:.2f}")

class AddFees(InterestRewards):
    def __init__(self, name, balance):
        super().__init__(name, balance)
        self.fees = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= (amount + self.fees)
            print(f"Account {self.name} has withdrawn ${amount:.2f} and ${self.fees:.2f} as fees. Remaining balance is ${self.balance:.2f}")
        except BalanceException as e:
            print(str(e))



"""
Key Points

Inheritance Hierarchy:
BankAccount → InterestRewards → AddFees.

Polymorphism:
The deposit and withdraw methods are overridden in subclasses, showcasing polymorphism.

Encapsulation:
Account balance is encapsulated within the BankAccount class, and methods (deposit, withdraw, etc.) provide controlled access.

Exception Handling:
Custom exception BalanceException ensures robust error handling for invalid transactions.
"""