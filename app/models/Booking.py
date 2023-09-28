from app import db
from sqlalchemy.ext.hybrid import hybrid_property

class Booking():
    __tablename__ = 'bookings'
    __id = db.column('id', db.Integer, primary_key=True, autoincrement=True)
    __start_booking = db.column('start_booking', db.DateTime(100))
    __finish_booking = db.column('finish_booking',db.DateTime(100))
    __duration = db.column('duration', db.Integer)
    __amount_people = db.column('amount_people',db.Integer)
    # TODO: Agregar clave foránea hacia la tabla de usuarios (user_id)
    # TODO: Agregar clave foránea hacia la tabla de apartamentos (apartment_id)

    """Constructor
    Atributos:
        start_booking (str): Fecha de inicio de la reserva, máximo 100 caracteres.
        finish_booking (str): Fecha de finalización de la reserva, máximo 100 caracteres.
        duration (int): Duración de la reserva, máximo 3 dígitos.
        amount_people (int): Cantidad de personas de la reserva, máximo 3 dígitos.
    """
    def __init__(self, start_booking: str, finish_booking: str, duration: int, amount_people: int):
        self.__start_booking = start_booking
        self.__finish_booking = finish_booking
        self.__duration = duration
        self.__amount_people = amount_people

    # es para obtener el atributo

    @hybrid_property
    def id(self)->int:
        return self.__id
    @id.setter
    def id(self, id:int):
        self.__id = id

    @hybrid_property
    def start_booking(self)->str:
        return self.__start_booking
    @start_booking.setter
    def start_booking(self, start_booking:str):
        self.__start_booking = start_booking

    @hybrid_property
    def finish_booking(self)->str:
        return self.__finish_booking
    @finish_booking.setter
    def finish_booking(self, finish_booking:str):
        self.__finish_booking = finish_booking

    @hybrid_property
    def duration(self)->int:
        return self.__duration
    @duration.setter
    def duration(self, duration:int):
        self.__duration = duration

    @hybrid_property
    def amount_people(self)->int:
        return self.__amount_people
    @amount_people.setter
    def amount_people(self, amount_people:int):
        self.__amount_people = amount_people

    def __repr__(self) -> str:
        return f'Booking:(start_booking:{self.__start_booking}, finish_booking:{self.__finish_booking}, duration:{self.__duration}, amount_people:{self.__amount_people})'

    # TODO: Revisar de qué manera se puede comparar un objeto de tipo Booking con otro objeto de tipo Booking
    # def __eq__(self, __value:object ) -> bool:
    #     return self.start_booking == __value.start_booking and self.finish_booking == __value.finish_booking

    # dbeaver es como pgadmin

