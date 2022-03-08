class User:

    def __init__(self, name):
        self.name = name
        self.balance = 0

    def make_withdrawal(self, amount):
        self.balance -= amount

    def make_deposit(self, amount):
        self.balance += amount

    def display_user_balance(self):
        print(f"{self.name} has a balance of {self.balance}")

    def make_transfer(self, amount, friend):
        self.balance -= amount
        friend.balance += amount
        print(f"{self.name} has {self.balance} remaining. {friend.name} has {friend.balance} remaining.")

ernesto = User("Ernesto")
michael = User("Michael")
henry = User("Henry")
ernesto.make_deposit(300)
ernesto.make_deposit(200)
ernesto.make_deposit(100)
ernesto.display_user_balance()
michael.make_deposit (200)
michael.make_deposit (200)
michael.make_withdrawal (100)
michael.make_withdrawal (200)
michael.display_user_balance()
henry.make_deposit (500)
henry.make_withdrawal (100)
henry.make_withdrawal (200)
henry.make_withdrawal (200)
henry.display_user_balance()
ernesto.make_transfer(200, michael)
