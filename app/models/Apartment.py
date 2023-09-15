from .. import db
from sqlalchemy.ext.hybrid import hybrid_property

class Apartment(db.Model):
    __tablename__ = 'apartments'
    id = db.Column('Id', db.Integer, primary_key=True, autoincrement=True)
    number = db.Column('Number', db.Integer)
    size = db.Column('Size', db.Integer)
    amount_rooms = db.Column('Amount_rooms',db.Integer)
    features = db.Column('Features', db.String(500))
    availability = db.Column('Availability',db.Boolean)
    lease = db.Column('Lease', db.Float)
    address = db.Column('Address', db.String(150))

    """Constructor
    Atributos:
        number (int): Número del apartamento, máximo 3 dígitos.
        size (int): Tamaño del apartamento, máximo 3 dígitos.
        amount_rooms (int): Cantidad de habitaciones del apartamento, máximo 3 dígitos.
        features (str): Características del apartamento, máximo 500 caracteres.	
        availability (bool): Disponibilidad del apartamento, True si está disponible o False si no lo está.
        lease (float): Arriendo del apartamento, máximo 10 dígitos.
        address (str): Dirección del apartamento, máximo 150 caracteres.
    """
    
    def __init__(self, number: int, size: int, amount_rooms: int, features: str, availability: bool, lease: float, address: str):
        self.__number = number
        self.__size = size
        self.__amount_rooms = amount_rooms
        self.__features = features
        self.__availability = availability
        self.__lease = lease
        self.__address = address

    @hybrid_property
    def id(self) -> int:
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id
    
    @hybrid_property
    def number(self) -> int:
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @hybrid_property
    def size(self) -> int:
        return self.__size
    @size.setter
    def size(self, size: int):
        self.__size = size
    
    @hybrid_property
    def amount_rooms(self) -> int:
        return self.__amount_rooms
    @amount_rooms.setter
    def amount_rooms(self, amount_rooms: int):
        self.__amount_rooms = amount_rooms
    
    @hybrid_property
    def features(self) -> str:
        return self.__features
    @features.setter
    def features(self, features: str):
        self.__features = features
    
    @hybrid_property
    def availability(self) -> bool:
        return self.__availability
    @availability.setter
    def availability(self, availability: bool):
        self.__availability = availability
    
    @hybrid_property
    def lease(self) -> float:
        return self.__lease
    @lease.setter
    def lease(self, lease: float):
        self.__lease = lease
    
    @hybrid_property
    def address(self) -> str:
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    def __repr__(self) -> str:
        return f'Apartment(number={self.number}, size={self.size}, amount_rooms={self.amount_rooms}, features={self.features}, availability={self.availability}, lease={self.lease}, address={self.address})'

    # ¿Cuándo un apartamento es igual?
    def __eq__(self, __value: object) -> bool:
        return self.number == __value.number