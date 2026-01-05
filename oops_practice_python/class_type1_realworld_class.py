class BankAccount():
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount <=0:
            raise ValueError("Deposit amount must be positive! ")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient Funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance

# Bank Account is the class, Account State is instance attribute, Methods are action and Rules imlemented in the logic.
# Key characteristic of real-world modeling-
# - Miantain State, Represents Entities, Have logn-lived instance and Map closely to domain language