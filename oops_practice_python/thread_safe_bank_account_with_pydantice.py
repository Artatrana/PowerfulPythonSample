from datetime import  datetime
from threading import Lock
from typing import Dict, List, Any

from pydantic import BaseModel, Field, PrivateAttr

class BankAccount(BaseModel):
    account_number: str
    owner_name: str
    balance: int = Field(ge=0)

    # Private (Not part of the model schema)
    _lock: Lock= PrivateAttr(default_factory=Lock)
    _audit_log: List[Dict] = PrivateAttr(default_factory=list )

    def _log_audit(self, action, amount, old_balance, new_balance):
        self._audit_log.append({
            "timestamp": datetime.utcnow().isoformat(),
            "action": action,
            "amount": amount,
            "old_balance": old_balance,
            "new_balance": new_balance
        })

    def deposit(self, amount: int):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        with self._lock:
            old_balance = self.balance
            new_balance = old_balance + amount
            self.balance = new_balance
            self._log_audit("DEPOSIT", amount, old_balance, new_balance)

    def withdraw(self, amount: int):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        with self._lock:
            old_balance = self.balance
            if amount > old_balance:
                raise ValueError("Insufficient funds")

            new_balance = old_balance - amount
            self.balance = new_balance
            self._log_audit("WITHDRAW", -amount, old_balance, new_balance)

    def get_audit(self):
        with self._lock:
            return self._audit_log.copy()

# Example Use cases
account = BankAccount(
account_number="123",
    owner_name="Ramesh",
    balance="1000"  # auto-converted
)

account.deposit(500)
account.withdraw(300)

print(account.balance)
print( account.get_audit())








