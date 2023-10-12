from app.models import Role
from app.repositories import RoleRepository

"""
En este servicio van todas las funciones referidas al rol.
Buscar todos los roles, buscar un rol por id, crear un rol, 
actualizar un rol, eliminar un rol.
"""

class RoleService:
    def __init__(self):
        self.__repo = RoleRepository() #se crea el repositorio para poder usar sus métodos(se instancia)

    def create(self, entity: Role) -> Role:
        return self.__repo.create(entity)
    
    def update(self, entity: Role, id: int) -> Role:
        return self.__repo.update(entity, id)
    
    def find_by_id(self, id: int) -> Role:
        return self.__repo.find_by_id(id)
    
    def find_all(self) -> list:
        return self.__repo.find_all()
    
    def delete(self, id: int) -> Role:
        return self.__repo.delete(id)