# Factory: Creates objects without exposing the creation logic to the caller and decides which object to create
# based on input or context.
# For example, when you order a vehicle, you don’t directly create a car or a bike—the factory decides which vehicle to
# give you based on your request.
# What is a Factory Method:
# The Factory Method defines an interface for creating an object but let subclass to decide which object to instantiate
# It helps you avoid tight coupling between object creation and usage ?
# Object creation logic is centralized
# Client doesn't care which class created it
# Easy to add new type without changing client logic

# When to use Factory Method
# You don't know which object type you will need till run-time
    # You want to follow Open/Closed principle ?
# You want to avoid many if/else scattered across the code

from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class EmailNotification(Notification):
    def send(self, message: str):
        print(f"Sending Email: {message}")

class SMSNotification(Notification):
    def send(self, message: str):
        print(f"Sending SMS {message}")

# Create the Factory method
class NotificationFactory:
    @staticmethod
    def create_notification(channel: str) -> Notification:
        if channel == "email":
            return EmailNotification()
        elif channel == "SMS":
            return SMSNotification()
        else:
            raise ValueError("Unsupported notification type")

# Use factory method
def notify_user(channel: str, message: str):
    notification = NotificationFactory.create_notification(channel)
    notification.send(message)

notify_user("email", "Your report is ready")
notify_user("SMS", "OTP: 123455")

# Show a more OOP-heavy version (subclass-based factory)
# Compare Factory vs Abstract Factory
# Factory Method vs Dependency Injection
# Map this to a real data engineering use case (Spark readers, DB connectors)






