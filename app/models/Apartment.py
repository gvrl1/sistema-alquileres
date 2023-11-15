from app import db
from sqlalchemy.ext.hybrid import hybrid_property

class Apartment(db.Model):
    __tablename__ = 'apartments'
    __id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    __number_of_apartment = db.Column('number_of_apartment', db.Integer)
    __size = db.Column('size', db.Integer)
    __amount_rooms = db.Column('amount_rooms',db.Integer)
    __features = db.Column('features', db.String(500))
    __availability = db.Column('availability',db.Boolean)
    __lease = db.Column('lease', db.Float)
    __address = db.Column('address', db.String(150))
    apartment_bookings = db.relationship('Booking', backref='apartment')

    """Constructor
    Atributos:
        number_of_apartment (int): Número del apartamento, máximo 3 dígitos.
        size (int): Tamaño del apartamento, máximo 3 dígitos.
        amount_rooms (int): Cantidad de habitaciones del apartamento, máximo 4 habitaciones.
        features (str): Características del apartamento, máximo 500 caracteres.	
        availability (bool): Disponibilidad del apartamento, True si está disponible o False si no lo está.
        lease (float): Arriendo del apartamento, máximo 10 dígitos.
        address (str): Dirección del apartamento, máximo 150 caracteres.
    """
    
    def __init__(self, number_of_apartment: int, size: int, amount_rooms: int, features: str, availability: bool, lease: float, address: str):
        self.__number_of_apartment = number_of_apartment
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
    def number_of_apartment(self) -> int:
        return self.__number_of_apartment
    @number_of_apartment.setter
    def number_of_apartment(self, number_of_apartment: int):
        self.__number_of_apartment = number_of_apartment

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
        return f'Apartment(number_of_apartment={self.__number_of_apartment}, size={self.__size}, amount_rooms={self.__amount_rooms}, features={self.__features}, availability={self.__availability}, lease={self.__lease}, address={self.__address})'

    # ¿Cuándo un apartamento es igual?
    def __eq__(self, __value: object) -> bool:
        return self.__number_of_apartment == __value.__number_of_apartment