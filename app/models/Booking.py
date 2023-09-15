from app import db
from sqlalchemy.ext.hybrid import hybrid_property

'''
define attributes and methods of class and persist users
'''


class Booking():
    __table_name = 'bookings'
    __start_booking = db.column('start_booking', db.String(100))
    __finish_booking = db.column('finish_booking',db.String(100))
    __durations = db.column('durations',db.int(100))
    __num_booking = db.column('num_booking',db.int(100))
    __amount_people = db.column('amount_people',db.int(100))


def __init__(self, start_booking:str, finish_booking:str, durations:str, num_booking:str, amount_people:str):
    self.start_booking = start_booking
    self.finish_booking = finish_booking
    self.durations = durations
    self.num_booking = num_booking
    self.amount_people = amount_people


# es para obtener el atributo
    
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
def durations(self)->str:
    return self.__durations

@durations.setter
def durations(self, durations:str):
    self.__durations = durations

@hybrid_property
def num_booking(self)->str:
    return self.__num_booking

@num_booking.setter
def num_booking(self, num_booking:str):
    self.__num_booking = num_booking

@hybrid_property
def amount_people(self)->str:
    return self.__amount_people

@amount_people.setter
def amount_people(self, amount_people:str):
    self.__amount_people = amount_people



# def __repr__(self) -> str:
#     return f'Booking:(start_booking:{self.start_booking}, finish_booking:{self.finish_booking}, durations:{self.durations}, num_booking:{self.num_booking}, amount_people:{self.amount_people})'

# def __eq__(self, value:object ) -> bool:
#     return self.start_booking == __value.start_booking and self.finish_booking == __value.finish_booking

# dbeaver es como pgadmin

