## Adapter Patter (If a class exists only to make two mismatched interfaces talk -> it's an adaptor)

# Intent: Allow two incompatible interface to work together by converting one interface to another that the client expects.
# Real‑World Analogy
# A power plug adapter that allows a US plug fit into a European socket.
# Real Applications:
# - JDBC Drivers adapting different databases to a common interfaces
# - Payment gateway(Stripe, PayPal) behind a unified payment API
# When to Use
# - Integrating legacy systems
# - Working with third-party libraries
# - Migrating old API to new one

# # Scenario
# Imagine you are building a payment processing system. Your system currently work with paypal, but now you need to
# integrate Stripe. Their interfaces are different:
# * PayPal has a method send_payment(amount)
# * Stripe has a method make_payment(amount_in_cents)
# Instead of changing your whole system to support Stripe, we can use an adaptor so both payment system can be used interchangeably

# Step 1 - Define target interface
class PaymentProcessor:
    def pay(self, amount: float):
        raise NotImplementedError("This method should be overridden")

# Step 2: Existing system class
class PayPal(PaymentProcessor):
    def pay(self, amount: float):
        print(f"Paying ${amount} using PayPal.")

# Step 3: Adaptee(new system with incompatible interface)
class Stripe:
    def make_payment(self, amount_in_cents: float):
        print(f"Paying {amount_in_cents} cents using Stripe.")

# Adapter
class StripeAdapter(PaymentProcessor):
    def __init__(self, stripe: Stripe):
        self.stripe = stripe

    def pay(self, amount: float):
        # Convert dollars to cents because Stripe expects cents
        amount_in_cents = int(amount * 100)
        self.stripe.make_payment(amount_in_cents)


def process_payment(processor: PaymentProcessor, amount: float):
    processor.pay(amount)

# using PayPal
paypal = PayPal()
process_payment(paypal,50)

stripe = Stripe()
stripe_adapter = StripeAdapter(stripe)
process_payment(stripe_adapter,50 )

################################################
# Scenario 2: Your application expects structured JSON logs, but logger only support plain text.
# Your system expects: log(level, message, metadata)
# Legacy logger supports: write(string)
# We’ll use an Adapter to bridge this gap.

# Step 1: Target interface( What your app expects)
from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, level: str, message: str, metadata: dict | None = None):
        pass

class LegacyFileLogger:
    def write(self,text: str):
        print(f"[LEGACY] {text}")

import json
from datetime import datetime

class LegacyLoggerAdapter(Logger):
    def __init__(self, legacy_logger: LegacyFileLogger):
        self.legacy_logger = legacy_logger

    def log(self, level: str, message: str, metadata: dict | None = None ):
        payload = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": level,
            "message": message,
            "metadata": metadata or {}
        }

        # Translate structured data → plain string
        self.legacy_logger.write(json.dumps(payload))

# Client Code unchanged
def process_log(logger: Logger):
    logger.log(
        level="INFO",
        message="Order processed",
        metadata={"order_id": 123, "amount": 49.99}
    )

    



