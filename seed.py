from model import DisasterEvent, connect_to_db, db
from server import app
import csv, os

def get_natural_disasters_data(csv_file):

    events = []

    event_counts = {}

    with open(csv_file) as data:
        disaster_data = list(csv.reader(data))

        for i in range(1, len(disaster_data)):
            row = disaster_data[i]
            state, date, event_type = row[5], str(row[10]), row[8].lower()

            event_counts[(state, date, event_type)] = event_counts.get((state, date, event_type), 0) + 1
        
        for event in event_counts:
            state, date, event_type = event[0], event[1], event[2]
            count = event_counts[event]

            events.append( { 'state': state,
                             'date': date,
                             'type': event_type,
                             'count': count })

    return events


def load_events_into_db(events):
    
    for event in events:
        state, date, incident_type, count = (event['state'],
                                            event['date'],
                                            event['type'],
                                            event['count'])
        
        event = DisasterEvent(state=state,
                              incident_type=incident_type,
                              start_date=date,
                              count=count)

        db.session.add(event)

    db.session.commit()


if __name__ == '__main__':
    connect_to_db(app, os.environ.get('DATABASE_URL'))
    
    db.create_all()

    events = get_natural_disasters_data('DisasterDeclarationsSummaries.csv')
    load_events_into_db(events)