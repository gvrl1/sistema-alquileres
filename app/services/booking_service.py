from app.models import Booking
from app.repositories import BookingRepository

"""
En este servicio van todas las funciones referidas a la reserva.
Buscar todas las reservas, buscar una reserva por id, crear una reserva.
"""

class BookingService:
    def __init__(self):
        self.__repo = BookingRepository()

    def create(self, entity: Booking) -> Booking:
        return self.__repo.create(entity)
    
    def find_all(self) -> list:
        return self.__repo.find_all()
    
    def find_by_id(self, id: int) -> Booking:
        return self.__repo.find_by_id(id)
    
    def update(self, entity: Booking, id: int) -> Booking:
        return self.__repo.update(entity, id)