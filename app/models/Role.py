from app import db
from sqlalchemy.ext.hybrid import hybrid_property
from .relationships import association_table

class Role(db.Model):
    __tablename__ = 'roles'
    __id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    __name = db.Column('name', db.String(100))
    __description = db.Column('description', db.String(100))
    users = db.relationship("User", secondary=association_table, back_populates='roles')

    """ Constructor
    Atributos:
        name (str): Nombre del rol, máximo 100 caracteres.
        description (str): Descripción del rol, máximo 100 caracteres.
    """

    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description

    @hybrid_property
    def id(self) -> int:
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id
    
    @hybrid_property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @hybrid_property
    def description(self) -> str:
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    def __repr__(self) -> str:
        return f'Role (name={self.__name} , description={self.__description})'
    
    def __eq__(self, __value: object) -> bool:
        return self.__name == __value.name
    