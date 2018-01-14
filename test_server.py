from server import app
from unittest import TestCase
from model import connect_to_db, db, example_data, DisasterEvent

class FlaskTestsBasic(TestCase):

    def setUp(self):

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_index(self):

        result = self.client.get('/')

        self.assertIn('Filter by', result.data)
        self.assertIn('# of Occurences', result.data)
        self.assertIn('US Natural Disasters', result.data)

if __name__ == '__main__':
    import unittest

    unittest.main()