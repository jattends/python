#its just a NAME CONVENTION only.

class BankAccount:
    def __init__(self):
        self.__balance = 1000  #__this is denote at private / but this private will be acesss in python case out side class

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount!")

    def get_balance(self):
        return self.__balance
account = BankAccount()
account.deposit(500)
print(account.get_balance())