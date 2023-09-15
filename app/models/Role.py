from .. import db
from sqlalchemy.ext.hybrid import hybrid_property

class Role:
    __tablename__ = 'roles'

    __description = db.Column('description', db.String(100))

    """ Constructor
    Atributos:
        description (str): Descripción del rol, máximo 100 caracteres.
    """

    def __init__(self, description: str):
        self.description = description

    @hybrid_property
    def description(self)->str:
        return self.__description
    
    @description.setter
    def description(self, description:str):
        self.__description = description

    def __repr__(self) -> str:
        return f'Role (description={self.description})'
    
    def __eq__(self, __value: object) -> bool:
        return self.description == __value.description
    