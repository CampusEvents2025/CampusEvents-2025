from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    event_date = db.Column(db.String(10), nullable=False)   # renamed
    location = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.Date, default=date.today)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "date": self.event_date,   # return as "date" for API compatibility
            "location": self.location
        }
