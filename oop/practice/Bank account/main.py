from Bank_account import *

Islam = BankAccount("Islam", 1000)
Islam.getBalance()
Islam.withdraw(500)
Islam.deposit(500)

Fatma = BankAccount("Fatma", 0)

Islam.transfer(Fatma, 500)
Islam.getBalance()
Fatma.getBalance()

Saad = InterestRewards("Saad", 0)
Saad.deposit(1000)  # Account Saad has deposited $1000. New balance is $1010.0
Saad.getBalance()  # Account Saad has balance of $1010.0

Nour = AddFees("Nour", 1005)
Nour.withdraw(500) # Account Nour has withdrawn $500 and $5 as fees. Remaining balance is $500
Nour.getBalance()  