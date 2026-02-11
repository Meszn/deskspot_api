from app.extensions import ma
from app.models.user import User
from app.models.desk import Desk
from app.models.booking import Booking

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ('password_hash',) # Şifreyi asla geri döndürme!

class DeskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Desk
        load_instance = True

class BookingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Booking
        load_instance = True
        include_fk = True # Foreign key'leri göster