from server import app
from unittest import TestCase
from model import connect_to_db, db, example_data, DisasterEvent
from datetime import datetime

class FlaskTestsBasic(TestCase):

    def setUp(self):

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_index(self):

        result = self.client.get('/')

        self.assertIn('Filter by', result.data)
        self.assertIn('# of Occurences', result.data)
        self.assertIn('US Natural Disasters', result.data)


class FlaskTestsDatabase(TestCase):

    def setUp(self):

        self.client = app.test_client()
        app.config['TESTING'] = True

        connect_to_db(app, "postgresql:///testdb")
        db.create_all()
        example_data()

    def tearDown(self):
        
        db.session.close()
        db.drop_all()

    def test_valid_query_1(self):

        inputs = {
            'from': '1970-01-01',
            'to': '1990-01-01',
            'event_type': ['Drought', 'Fire']
        }

        result = self.client.get('/api/events', query_string=inputs)

        self.assertIn('VT', result.data)
        self.assertIn('1973/11/27', result.data)

    def test_valid_query_2(self):

        inputs = {
            'from': '1970-01-01',
            'to': '1990-01-01',
            'event_type': ['Drought', 'Earthquake']
        }

        result = self.client.get('/api/events', query_string=inputs)
        
        self.assertIn('VT', result.data)
        self.assertIn('1973/11/27', result.data)
        self.assertIn('Drought', result.data)
        self.assertIn('CA', result.data)
        self.assertIn('1989/10/17', result.data)

    def test_invalid_query(self):

        inputs = {
            'from': '2009-01-01',
            'to': '1998-01-01',
            'event_type': ['Drought', 'Earthquake']
        }

        result = self.client.get('/api/events', query_string=inputs)
        
        self.assertEqual(400, result.status_code)


if __name__ == '__main__':
    import unittest

    unittest.main()