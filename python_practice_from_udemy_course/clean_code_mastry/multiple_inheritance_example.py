class Logger:
    def __init__(self, *args, **kwargs):
        self.log_messages=[]
        #super().__init__(*args, **kwargs)

    def log(self, message):
        self.log_messages.append(message)
        print(f"[LOG] {message}")

class DatabaseHandler:
    def __init__(self, *args, **kwargs):
        print("Connecting to the database...")
        self.db_connection = self.connect_to_db()
        #super().__init__(*args, **kwargs)

    @staticmethod
    def connect_to_db():
        return {"status": "connected"}

    def save(self):
        if not hasattr(self, "db_connection"):
            raise RuntimeError("Database connection is missing")
        print(f"Saving {self.__dict__} to database...")

class User(Logger, DatabaseHandler):
    def __init__(self, user_id, name):
        super().__init__()
        self.user_id = user_id
        self.name = name


u = User(101, "Alice")
print(User.mro())
u.log("User Created")
u.save()


