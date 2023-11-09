from app.models import Booking
from app.repositories import BookingRepository
from app.services import UserService, ApartmentService

"""
En este servicio van todas las funciones referidas a la reserva.
Buscar todas las reservas, buscar una reserva por id, crear una reserva.
"""

class BookingService:
    def __init__(self):
        self.__repo = BookingRepository()

    def create(self, entity: Booking, user_id: int, apartment_id: int) -> Booking:
        user = UserService().find_by_id(user_id)
        apartment = ApartmentService().find_by_id(apartment_id)
        entity.user = user
        entity.apartment = apartment
        return self.__repo.create(entity)
    
    def find_all(self) -> list:
        return self.__repo.find_all()
    
    def find_by_id(self, id: int) -> Booking:
        return self.__repo.find_by_id(id)
    
    def update(self, entity: Booking, id: int) -> Booking:
        return self.__repo.update(entity, id)