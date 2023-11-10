from app.models import User
from app import db
from app.repositories import Create, Read, Update, Delete

class UserRepository(Create, Read, Update, Delete):

    def __init__(self):
        self.__model = User
    
    def create(self, entity: User) -> User:
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def delete(self, id: int) -> User:
        entity = self.find_by_id(id)
        db.session.delete(entity)
        db.session.commit()
        return entity
    
    def find_by_id(self, id: int) -> User:
        return db.session.query(self.__model).filter(self.__model.id == id).one()
    
    def find_all(self) -> list:
        return db.session.query(self.__model).all()
    
    def find_by_email(self, email: str) -> User:
        return db.session.query(self.__model).filter(self.__model.email_address == email).one()

    def update(self, user: User, id: int) -> User:
        entity = self.find_by_id(id)
        entity.name = user.name
        entity.lastname = user.lastname
        entity.phone_number = user.phone_number
        entity.email_address = user.email_address
        db.session.add(entity)
        db.session.commit()
        return entity
    