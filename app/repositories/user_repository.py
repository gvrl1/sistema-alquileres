from app.models import User
from app import db
from app.repositories import Create, Read, Update, Delete

class UserRepository(Create, Read, Update, Delete):
    
    def __init__(self):
        self.__model = User

    def create(self, entity: User) -> User:
        try:
            db.session.add(entity)
            db.session.commit()
            return entity
        except:
            db.session.rollback()
            raise

    # def find_by_id(self, id: int) -> User:
    #     return db.session.query(self.__model).filter(self.__model.id == id).one()
    
    # def find_all(self) -> list:
    #     return db.session.query(self.__model).all()
    
    # def find_by_username(self, username: str) -> User:
    #     return db.session.query(self.__model).filter(self.__model.username == username).one()
