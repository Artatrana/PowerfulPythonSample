import datetime
import  csv

from dateutil.parser import parse

class RecordsByDate:
    def __init__(self,data):
        self.data = data

    @classmethod
    def read_csv(cls, path):
        data = {}
        with open(path) as handle:
            for row in csv.DictReader(handle):
                when = parse(row['ent_date']).date()
                print(when)
                data[when] = row
        return cls(data)

    def __getitem__(self, when):
        return self.data[when]
