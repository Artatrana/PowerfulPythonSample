# We mainly build Two kinds of objects
# 1️⃣ Entity objects (data-centric)
# - It holds state
# - Represent "things"
class User:
    def __init__(self, name):
        self.name = name
# Example
# - User
# - Order
# BatteryCell
# Transaction

# 2️⃣ Service / Role objects (behavior-centric)
# - Manily holds little or no data
# - Exist to do somthing

class EmailSender:
    def send(self, msg):
        ...

# Examples:
# - Logger
# - Validator
# - Serializer
# - Data Loader
# - Model trainer

# ### Why create an object at all if there’s no data?
# Because
# - behavior may depend on configuration
# - behavior may change by implementation
# - behavior needs polymorphism


class S3Storage(Storage):
    def save(self, data):
        print("Saving to S3")

class LocalStorage(Storage):
    def save(self, data):
        print("Saving locally")

def persist(storage: Storage, data):
    storage.save(data)

# Here persist() does not care what object it gets. Its only care about behavior contract

# 6. But these objects do have state (just not domain data)
# Even behavior objects usually have state, just not business data.

class S3Storage(Storage):
    def __init__(self, bucket, region):
        self.bucket = bucket
        self.region = region

# This is:
# - configuration state
# - operational state
# - not domain/entity data

# 7- Why not just use functions ?
# - Harder to swap implementations
# - Harder to inject dependencies
# - Harder to test
# - Harder to extend

# You gain:
# polymorphism
# dependency inversion
# clean architecture
# testability (mock Storage)

# 8. The real purpose of abstract classes (core idea) : Abstract classes exist to decouple “what needs to be done” from “how it’s done.”
#
# They:
# define roles
# define capabilities
# define interfaces
#
# NOT:
# data models
# storage schemas
# entity state

# 9. Mental model that will lock this in
# Think in terms of roles, not things
# Something that can save data
# Something that can send notification
# Something that can validate inputse
