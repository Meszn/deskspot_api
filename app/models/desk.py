from app.extensions import db

class Desk(db.Model):
    __tablename__ = 'desks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)  # Örn: Masa-A1
    location = db.Column(db.String(100))             # Örn: 2. Kat, Pencere kenarı
    is_active = db.Column(db.Boolean, default=True)