
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from model import DisasterEvent, db, connect_to_db
from datetime import date, datetime

app = Flask(__name__)

@app.route('/events-list')
def displays_events():
    """
    Renders table filter page.

    """
    
    return render_template('/events.html')


@app.route('/api/events', methods=['GET'])
def get_events():

    events_info = []

    from_date = parse_date_input(request.args.get('from'))

    to_date = parse_date_input(request.args.get('to'))

    if validate_date_params(from_date, to_date) is 'invalid':
        return jsonify([]), 400

    event_types = request.args.getlist('event_type')
    
    queried_events = make_query_to_db(from_date, to_date, event_types)
    

    for event in queried_events:
        date = event.start_date.strftime('%Y/%m/%d')
        events_info.append({ 'disasterId': event.disaster_id,
                             'state': event.state,
                             'incidentType': event.incident_type,
                             'startDate': date,
                             'count': event.count })

    return jsonify(events_info)


def parse_date_input(date):
    """
    Converts unicode string to datetime object.

    """

    return datetime.strptime(date, '%Y-%m-%d')



def validate_date_params(from_date, to_date):
    """
    Checks that dates entered by user are valid.

    """
    if to_date < from_date:
        return 'invalid'
    


def make_query_to_db(from_date, to_date, event_types):
    """
    Makes database query based on validated form inputs.

    """

    q = DisasterEvent.query

    filtered_events = q.filter( (DisasterEvent.incident_type.in_(event_types))
                                & (DisasterEvent.start_date >= from_date)
                                & (DisasterEvent.start_date <= to_date)
                              ).order_by('start_date').all()

    return filtered_events



if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0', port=3000)
