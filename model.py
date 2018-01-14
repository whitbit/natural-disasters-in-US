from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DisasterEvent(db.Model):

    __tablename__ = 'disasters'

    disaster_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    state = db.Column(db.String(2), nullable=False)
    incident_type = db.Column(db.String(200), nullable=False, index=True)
    start_date = db.Column(db.DateTime, index=True)
    count = db.Column(db.Integer)

    def __repr__(self):
        """ Provides helpful representation when printed."""

        return "<Disaster id={}, state={}, type={}, date={}>".format(self.disaster_id,
                                                                   self.state,
                                                                   self.incident_type,
                                                                   self.start_date)


def example_data():

    DisasterEvent.query.delete()

    event1 = DisasterEvent(state='CA',
                           incident_type='Earthquake',
                           start_date='10/17/1989',
                           count=5)
    event2 = DisasterEvent(state='CA',
                           incident_type='Fire',
                           start_date='12/11/2017',
                           count=3)
    event3 = DisasterEvent(state='VT',
                          incident_type='Drought',
                          start_date='11/27/1973',
                          count=2)

    db.session.add_all([event1, event2, event3])
    db.session.commit()
    

def connect_to_db(app, db_uri=None):

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri or 'postgres:///disaster_event_counts'
    app.config['SQLCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

if __name__ == '__main__':
    from server import app
    connect_to_db(app)