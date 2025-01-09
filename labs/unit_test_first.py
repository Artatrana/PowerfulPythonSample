import unittest
from testrecords import RecordsByDate
from datetime import date

class TestRecordsByDate(unittest.TestCase):
    def test_load_csv(self):
        recs = RecordsByDate.read_csv('testdata.csv')
        expected = {
            'date': '2020-11-30',
            'email': 'artatrana.pujahari@gmail.com',
            'status': 'active',
            'source': 'facebook',
        }

        actual = recs[date(2020,11,30)]
        self.assertEqual = (expected,actual )



