# Add logging/audit trail
# Add thread-safety
# Extend this into SavingsAccount / CreditAccount
# Map this class to a DB / ORM model

# Type-2 Python class 2. To Bundle Data + Functions Together (Encapsulation)
class BankAccount():
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self._balance = balance # protected

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive! ")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive! ")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def get_balance(self):
        return self._balance

# Class with property

class BankAccount2:
    def __init__(self, account_numer,owner_name, balance=0 ):
        self.account_number = account_numer
        self.owner_name = owner_name
        self._balance = balance

    @property
    def balance(self):
        """ Read only access to balance"""
        return self._balance

    @balance.setter
    def balance(self, value):
        """
        set balance directly only if business rule allow it.
        Useful for admin corrections, migrate, or reconciliation.
        """
        if value <0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

# ================
# Implement the Bank Account Class with Audit Log
import datetime
from typing import List, Dict

class BankAccountWithAudit:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self._balance = balance
        self._audit_log: List[Dict] = []

    @property
    def balance(self):
        return self._balance

    def _log_audit(self, action, amount, old_balance, new_balance):
        self._audit_log.append({
            "timestamp": datetime.utcnow().isoformat(),
            "action": action,
            "amount": amount,
            "old_balance": old_balance,
            "new_balance": new_balance
        })

    def _update_balance(self, delta, action):
        old_balance = self._balance
        new_balance = old_balance + delta

        if new_balance < 0:
            raise ValueError("Insufficient funds")

        self._balance = new_balance
        self._log_audit(action, delta, old_balance, new_balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._update_balance(amount, action="DEPOSIT")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        self._update_balance(-amount, action="WITHDRAW")

    def audit_log(self):
        return self._audit_log

