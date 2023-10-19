from app.models import Booking
from app import db
from app.repositories import Create


class BookingRepository(Create):
    
    def __init__(self):
        self.__model = Booking

    def create(self, entity: Booking) -> Booking:
        db.session.add(entity)
        db.session.commit()
        return entity
        
    def find_all(self) -> list:
        return db.session.query(self.__model).all()
    
    def find_by_id(self, id: int) -> Booking:
        return db.session.query(self.__model).filter(self.__model.id == id).one()
    
    def update(self, Booking: Booking, id: int) -> Booking:
            entity = self.find_by_id(id)
            entity.start_booking = Booking.start_booking
            entity.finish_booking = Booking.finish_booking
            entity.duration = Booking.duration
            entity.amount_people = Booking.amount_people
            db.session.add(entity)
            db.session.commit()
            return entity

