# 1. Represent Real-World Things (Modeling Objects)
# Real world: A bank account exists in the real world.
from PyQt6.QtSql import transaction


class BankAccount:
    def __init__(self, account_number, owner):
        self.account_number = account_number
        self.owner = owner

# 2. Bundle Data + Functions Together (Encapsulation)
# Real world: Balance should only change via bank rules.
class BankAccount1:
    def __init__(self,account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
# Data + behavior live together
# Prevents random external changes

# 3. Create Multiple Objects of Same Template
# Real world: One bank, millions of accounts.

a1 = BankAccount1("A1", "Ramesh")
a2 = BankAccount1("A2", "Suresh")

# Same blueprint different instance

# 4. Maintain State Across Method Calls
# Real world: Your balance doesn't reset after each transaction

a1.deposit(100)
a1.deposit(50)

# State(_balance) presists
# This hard without classes

# 5. Improve Code Organization (Modular Design)
# Real world: Banking logic should not be scattered.
# account.py
class BankAccountExample:...
#
# transaction.py
class TransactionService:...

# Classes act as logical boundaries

# 6. Support Inheritance (Reuse Existing Code)
# Real world: Savings and Checking accounts share common behavior.

class SavingAccount(BankAccount1):
    def add_interest(self):
        self._balance *= 1.04

# Avoid duplicate
# Model real product hierarchy

# 7. Support Polymorphism (Same Name, Different Behavior)
# Real World: Different accounts calculate fees differently

class CheckingAccount(BankAccount):
    def calculate_fee(self):
        return 5

class SavingsAccount(BankAccount):
    def calculate_fee(self):
        return 0

def apply_fee(account):
    fee = account.calculate_fee()
# Same method name
# Behavior depends on object type

# 8. Create Custom Data Types
# Real world: A bank account is a domain object, not a dict

account = BankAccount("A1", "Ramesh")

# Stronger than:
account = {"id": "A1", "balance": 100}

# 9. Hide Internal Implementation (Abstraction)
# Real world: Customers don't know how balance is stored

class BankAccount2:
    @property
    def balance(self):
        return self._balance

# Here Internal Logic can change, but external USER stay uneffected


# 10. Maintain Clean Large-Scale Codebases
# Real world: Large banks = thousands of engineers.

# bank/
#  ├── accounts/
#  ├── loans/
#  ├── payments/
#  └── fraud/
#
#
# Each domain = set of classes
# Enables team ownership

# 11. Use Magic Methods (Operator Overloading)
# Real world: Transfer money using +

def __add__(self, other):
    self.deposit(other)
    return self

account + 100
# Improves expressiveness
# Reads like business language

# 12. Create Reusable Components / Frameworks
# Real world: Reuse transaction logic across products

class TransactionProcessor:
    def processor(self, account, amount):
        account.deposit(amount)

# lug into: Banking app, Wallet, Loan system

# 13. Implement Design Patterns
# Example: Strategy Pattern

# Real world: Different interest calculation strategies

class InterestStrategy:
    def calculate(self, balance):
        raise NotImplementedError

class HighInterest(InterestStrategy):
    def calculate(self, balance):
        return balance * 0.06

# Swap behavior without changing core code

# 14. Manage Resources (Context Managers)
# Real world: Database transactions must close safely

class Transaction:
    def __enter__(self):
        print('Start transactions')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('End transactions')

with Transaction():
    account.deposit(100)
#  Guarantees cleanup
#  Prevents leaks

# 15. Create Packages / Libraries / SDKs
# Real world: Banking SDK used by partners.

# bank_sdk/
#  ├── accounts.py
#  ├── transactions.py
#  ├── exceptions.py

# from bank_sdk.accounts import BankAccount
# Clean public API, Internal complexity hidden
