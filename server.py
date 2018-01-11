
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from model import DisasterEvent, db, connect_to_db

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/events', methods=['GET'])
def get_events():

    all_events = DisasterEvent.query.all()

    print all_events

    return jsonify({})

if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0', port=3000)
