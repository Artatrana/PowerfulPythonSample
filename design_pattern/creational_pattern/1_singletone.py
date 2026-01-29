# Singleton: Ensures that only one instance of a class exists and that everyone uses the same instance.
# For example, an application configuration or database connection should be created once; if multiple instances exist,
# different parts of the system may read or write conflicting values, causing inconsistency.
# 1. When do you need Singleton?
# - You need one shared resource ( e.g. Logging, config, DB Connection)
# - You want controlled access to that resource
# - You want to avoid creating multiple costly instances

# Real world example
# - Database connection – Only one connection pool shared by all parts of the program
# - Logging - One logger used across the application to avoid duplicate logs
# - Printer spooler - Only one print queue in a computer
# - Setting/Configuration Manager - Only one object holding app configuration

class SingletonMeta(type):
    __instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__( *args, **kwargs)
        return cls.__instance

class Logger(metaclass=SingletonMeta):
    def log(self, message):
        print(f"Log: {message}")

logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)  # True, same instance

logger1.log("Hello")
logger2.log("World")



