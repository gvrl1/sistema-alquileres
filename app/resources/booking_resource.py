from flask import Blueprint, jsonify, request
from ..services.booking_service import BookingService
from ..mapping.booking_schema import BookingSchema
from ..mapping.apartment_schema import ApartmentSchema

ps = ApartmentSchema(many=True) # Para devolver varios departamentos

booking = Blueprint('booking', __name__)

booking_schema = BookingSchema() # Para devolver una reserva
booking_service = BookingService()


@booking.route('/create', methods=['POST'])
def create():
    # Crear una reserva
    try:
        booking = booking_schema.load(request.json)
        return {"booking": booking_schema.dump(booking_service.create(booking))}, 200
    except Exception as e:
        e = str(e)
        return jsonify(f"{e}"), 400
    
@booking.route('/findall', methods=['GET'])
def find_all():
    try:
        return {"booking": ps.dump(booking_service.find_all())}, 200
    except Exception as e:
        e = str(e)
        return jsonify(e), 400
    
@booking.route('/findbyid/<int:id>', methods=['GET'])
def find_by_id(id):
    try:
        return {"booking": booking_schema.dump(booking_service.find_by_id(id))}, 200
    except Exception as e:
        e = str(e)
        return jsonify(e), 400
    
@booking.route('/update/<int:id>', methods=['POST'])
def update(id):
    try:
        booking = booking_schema.load(request.json)
        return {"booking updated": booking_schema.dump(booking_service.update(booking, id))}, 200
    except Exception as e:
        e = str(e)
        return jsonify(f"{e}"), 400

