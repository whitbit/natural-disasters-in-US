from model import NaturalDisasters, connect_to_db, db
from server import app
import csv

def get_natural_disasters_data(csv_file):

    events = []

    with open(csv_file) as data:
        disaster_data = csv.reader(data)

        for row in disaster_data:
            events.append({ 'state': row[5],
                            'date': row[10],
                            'type': row[8]})

    return events

def load_events_into_db(events):
    

print get_natural_disasters_data('DisasterDeclarationsSummaries.csv')