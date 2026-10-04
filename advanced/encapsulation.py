# Python Encapsulation

# Encapsulation means protecting data inside a class.


class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance


    def show_balance(self):
        print("Balance:", self.__balance)


    def deposit(self, amount):
        self.__balance += amount


# Create an object

account = BankAccount("Poria", 100)


# Show balance

account.show_balance()


# Add money

account.deposit(50)


# Show new balance

account.show_balance()
