""" In this module I am going to impliment some of the property example"""
from datetime import datetime

class Logger:
    @property
    def current_time(self):
        return datetime.utcnow().isoformat()

l = Logger()
print(l.current_time)
