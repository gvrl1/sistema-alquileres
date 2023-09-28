from app.models import User
from app.repositories import UserRepository
from werkzeug.security import generate_password_hash

"""
En este servicio van todas las funciones referidas al usuario.
Buscar todos los usuarios, buscar un usuario por id, crear un usuario, actualizar un usuario, eliminar un usuario.
"""

class UserService:

    def __init__(self):
        self.__repo = UserRepository()

    def create(self, entity: User) -> User:
        entity.password = generate_password_hash(entity.password)
        return self.__repo.create(entity)
    
    # def update(self, entity: User, id: int) -> User:
    #     return self.__repo.update(entity, id)
    
    # def find_all(self) -> list:
    #     return self.__repo.find_all()
    
    # def find_by_username(self, username: str) -> User:
    #     return self.__repo.find_by_username(username)
    
    # def find_by_id(self, id: int) -> User:
    #     return self.__repo.find_by_id(id)
    
    # # Puede ir en otro módulo
    # def check_auth(self, username, password):
    #     pass
    