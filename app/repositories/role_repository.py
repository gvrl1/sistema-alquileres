from app.models import Role
from app import db
from app.repositories import Create, Read, Update, Delete

class RoleRepository(Create, Update, Read, Delete):

    def __init__(self):
        self.__model = Role

    def create(self, entity: Role) -> Role:
        db.session.add(entity)
        db.session.commit()
        return entity 
    
    def update(self, role: Role, id: int) -> Role:
        entity = self.find_by_id(id)
        entity.name = role.name
        entity.description = role.description
        db.session.add(entity) 
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