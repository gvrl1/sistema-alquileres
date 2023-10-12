from app.models import Role
from app import db
from app.repositories import Create, Read, Update, Delete

class RoleRepository(Create, Update, Read, Delete):

    def __init__(self):
        self.__model = Role

    def create(self, entity: Role) -> Role: #se crea el rol (se persiste en la DB)
        db.session.add(entity) #se agrega el rol a la DB
        db.session.commit() #se guarda el rol en la DB/se confirman los cambios
        return entity #se devuelve el rol creado
    
    def update(self, role: Role, id: int) -> Role:
        entity = self.find_by_id(id)
        entity.name = role.name
        entity.description = role.description
        db.session.add(entity) #guarda la entidad sobreescrita con role(algo así)
        db.session.commit()
        return entity
    
    def find_by_id(self, id: int) -> Role:
        return db.session.query(self.__model).filter(self.__model.id == id).one()
    
    def find_all(self) -> list:
        return db.session.query(self.__model).all()
    
    def delete(self, id: int) -> Role:
        entity = self.find_by_id(id)
        db.session.delete(entity)
        db.session.commit()
        return entity