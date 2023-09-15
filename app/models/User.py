from .. import db
from sqlalchemy.ext.hybrid import hybrid_property

class User: 
    __tablename__ ='users'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(100))
    lastname = db.Column('lastname', db.String(100))
    phone_number = db.Column('phone_number', db.String(15))
    email_address = db.Column('email_address', db.String(100))
    # data_id = db.Column('data', ...)

    """ Constructor
    Atributos: 
        name (str): Nombre del usuario, máximo 100 caracteres.
        lastname (str): Apellido del usuario, máximo 100 caracteres.
        phone_number (str): Número de teléfono del usuario, máximo 15 dígitos.
        email_address (str): Dirección de correo electrónico del usuario, máximo 100 caracteres.
    """

    def __init__(self, name: str, lastname: str, phone_number: str, email_address: str):
        self.name = name
        self.lastname = lastname
        self.phone_number = phone_number
        self.email_address = email_address

    @hybrid_property
    def id(self)->str:
        return self.__id
    
    @id.setter
    def code(self, id:str):
        self.__id = id

    @hybrid_property
    def name(self)->str:
        return self.__name
    
    @name.setter
    def name(self, name:str):
        self.__name = name

    @hybrid_property
    def lastname(self)->str:
        return self.__lastname
    
    @lastname.setter
    def lastname(self, lastname:str):
        self.__lastname = lastname

    @hybrid_property
    def phone_number(self)->str:
        return self.__phone_number
    
    @phone_number.setter
    def phone_number(self, phone_number:str):
        self.__phone_number = phone_number
    
    @hybrid_property
    def email_address(self)->str:
        return self.__email_address
    
    @email_address.setter
    def email_address(self, email_address:str):
        self.__email_address = email_address

    def __repr__(self) -> str:
        return f'User (code={self.code}, name={self.name}, lastname={self.lastname}, phone_number={self.phone_number}, email_address={self.email_address})'

    def __eq__(self, __value: object) -> bool:
        return self.code == __value.code and self.name == __value.name 
    