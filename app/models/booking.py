from app.extensions import db
from datetime import datetime

class Booking(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    desk_id = db.Column(db.Integer, db.ForeignKey('desks.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # İlişkiler
    user = db.relationship('User', backref=db.backref('bookings', lazy=True))
    desk = db.relationship('Desk', backref=db.backref('bookings', lazy=True))