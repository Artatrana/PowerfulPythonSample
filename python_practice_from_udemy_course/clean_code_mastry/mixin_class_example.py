# Mixin class shoud not have a __init__ method

class CacheMixin:
    def cache_result(self, key, value):
        if not hasattr(self, "_chase"):
            self._chase = {}
        self._chase[key] = value

class LogMixin:
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")

class DatabaseMixin:
    def connection_to_db(self):
        self.db_connection = { "status":"connected"}

    def save(self):
        if not hasattr(self, "db_connection"):
            raise RuntimeError("Database connection is missing")
        print(f"Saving {self.__dict__} to database...")

class User(LogMixin, DatabaseMixin):
    def __init__(self, user_id, name):
        self.connection_to_db()
        self.user_id = user_id
        self.name = name


u = User(101, "Alice")
u.log("User created")
u.save()