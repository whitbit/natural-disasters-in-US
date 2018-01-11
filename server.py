
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from model import DisasterEvent, db, connect_to_db
from datetime import date

app = Flask(__name__)

@app.route('/events-list')
def displays_events():
    
    return render_template('/events.html')

@app.route('/api/events', methods=['GET'])
def get_events():

    start_date = request.args.get('startDate')
    event_type = request.args.get('type')
    
    events_list = []

    all_events = DisasterEvent.query.all()

    for event in all_events:
        date = event.start_date.strftime('%B %m, %Y')
        events_list.append({ 'disaster_id': event.disaster_id,
                             'state': event.state,
                             'incident_type': event.incident_type,
                             'start_date': date })

    return jsonify(events_list)

def parse_params(start_date, type):
    pass

def validate_params():
    pass

def make_query_to_db():
    pass



if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0', port=3000)
