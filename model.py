from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class NaturalDisasters(db.Model):

    __tablename__ = 'disasters'

    disaster_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    state = db.Column(db.String(2), nullable=False)
    incident_type = db.Column(db.String(200), nullable=False)
    start_date = db.Column(db.DateTime)

    def __repr__(self):
        """ Provides helpful representation when printed."""

        return "<Disaster id={}, state={}, type={}, date={}"

def connect_to_db(app, db_uri=None):

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri or 'postgres:///natural_disasters'
    app.config['SQLCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)

