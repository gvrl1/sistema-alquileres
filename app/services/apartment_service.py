from app.models import Apartment
from app.repositories import ApartmentRepository

"""
En este servicio van todas las funciones referidas al departamento.
Buscar todos los departamentos, buscar un departamento por id, crear un departamento, 
actualizar un departamento, eliminar un departamento.
"""

class ApartmentService:
    def __init__(self):
        self.__repo = ApartmentRepository()

    def create(self, entity: Apartment) -> Apartment:
        return self.__repo.create(entity)
    
    def update(self, entity: Apartment, id: int) -> Apartment:
        return self.__repo.update(entity, id)
    
    def find_by_id(self, id: int) -> Apartment:
        return self.__repo.find_by_id(id)
    
    def find_all(self) -> list:
        return self.__repo.find_all()
    
    def delete(self, id: int) -> Apartment:
        return self.__repo.delete(id)