# Bank accounts
# What do we need to keep track of?
#   - routing number
#   - balance
#   - deposits and withdrawal (transaction history)
#   - name
#   - account type (Checking, savings, etc)
#   - security code

# imagine if every function that does something on bank accounts has to look
# like this:
# def do_a_thing_with_an_account(routing: str, balance: int, history: List[??], name: str, ....)
#
# This would be terrible.
#
# We're going to learn about classes which will let us do this in a much nicer way:
#
# def do_a_thing_with_an_account(account: BankAccount) -> ...

# Classes & objects
# -----------------
#
# A class is like a "blueprint" that describes what objects of that class have
# in common. e.g. "car".  Objects are specific instances of a class.
# e.g. my Honda Odyssey.
#
# Objects have
#   - things they *know* (i.e. information they keep track of)
#   - things they *can do* (i.e. operations/functions we can do with an object)

# Example: class for bank accounts

class BankAccount:
    # __init__ is a special/magical function that
    # is called every time we want to create a new object
    # of this class.
    #
    # self is a special reference to the object being created.
    #   It always has to go first.
    def __init__(self, name: str, balance: int):

        # Save the initial values of name and balance
        # into 'fields' (i.e. variables within the object).
        self.name = name
        self.balance = balance

        # Note that __init__ automatically
        # returns a reference to the created object

    # Functions defined inside a class are called "methods".

    def print(self):
        print(f'{self.name} has a balance of {self.balance}.')

    def deposit(self, money: int):
        self.balance += money

    def withdraw(self, money: int) -> bool:
        if money > self.balance:
            print("Insufficient funds!!")
            return False
        else:
            self.balance -= money
            return True

    def transferTo(self, otherAccount: 'BankAccount', money: int):
        if self.withdraw(money):
            otherAccount.deposit(money)

def main():
    # We create a new object of a class by writing the name
    # of the class followed by parentheses.  It will
    # automatically call __init__.  Note that the
    # first 'self' parameter will be filled in automatically
    # by Python.
    b1 = BankAccount('Ian', 150)
    b2 = BankAccount('Riley', 3000)

    b1.print()     # Tell the b1 BankAccount object to run the print() method.
    # b1.deposit(10)
    # b1.print()
    # b2.print()
    b2.print()
    b2.transferTo(b1, 40000)
    b1.print()
    b2.print()

main()