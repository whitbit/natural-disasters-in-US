from model import DisasterEvent, connect_to_db, db
import datetime
from server import app
import csv, os

def get_natural_disasters_data(csv_file):

    events = []

    with open(csv_file) as data:
        disaster_data = list(csv.reader(data))

        for i in range(1, len(disaster_data)):
            row = disaster_data[i]
            events.append({ 'state': row[5],
                            'date': str(row[10][:10]),
                            'type': row[8]})

    return events

def load_events_into_db(events):
    
    for event in events:
        state, date, incident_type = (event['state'],
                                  event['date'],
                                  event['type'])
        
        event = DisasterEvent(state=state,
                              incident_type=incident_type,
                              start_date=date)

        db.session.add(event)

    db.session.commit()


if __name__ == '__main__':
    connect_to_db(app, os.environ.get('DATABASE_URL'))
    
    db.create_all()

    events = get_natural_disasters_data('DisasterDeclarationsSummaries.csv')
    load_events_into_db(events)