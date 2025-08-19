from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, Event
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    db.init_app(app)

    # Health check
    @app.route('/health')
    def health():
        return jsonify({'status': 'ok'})

    # Get all events
    @app.route('/events', methods=['GET'])
    def get_events():
        events = Event.query.all()
        return jsonify([e.to_dict() for e in events])

    # Create new event
    @app.route('/events', methods=['POST'])
    def create_event():
        data = request.get_json()
        ev = Event(
            title=data['title'],
            event_date=data['date'],   # ✅ match renamed column
            location=data['location']
        )
        db.session.add(ev)
        db.session.commit()
        return jsonify(ev.to_dict()), 201

    return app


app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()   # ✅ create tables if they don't exist
    app.run(port=5000, debug=True)
