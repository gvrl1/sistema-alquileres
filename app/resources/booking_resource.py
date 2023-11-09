from flask import Blueprint, jsonify, request
from ..services.booking_service import BookingService
from ..mapping.booking_schema import BookingSchema
from ..dto import ResponseBuilder

ps = BookingSchema(many=True) # Para devolver varios departamentos

booking = Blueprint('booking', __name__)

booking_schema = BookingSchema() # Para devolver una reserva
booking_service = BookingService()
response = ResponseBuilder()


@booking.route('/create', methods=['POST'])
def create():
    # Crear una reserva
    try:
        data = request.get_json()
        user_id = data['user_id']
        data.pop('user_id')
        apartment_id = data['apartment_id']
        data.pop('apartment_id')
        booking = booking_schema.load(data)
        response.add_status_code(200).add_message('Booking created!').add_data(
            {"booking created": booking_schema.dump(booking_service.create(booking, user_id, apartment_id))}
        )
        return jsonify(response.build()), response.status_code
    except Exception as e:
        e = str(e)
        response.add_status_code(400).add_message('An error occurred while creating a booking!').add_data({"error": e})
        return jsonify(response.build()), response.status_code
    
@booking.route('/findall', methods=['GET'])
def find_all():
    try:
        response.add_status_code(200).add_message('Bookings found!').add_data({"bookings": ps.dump(booking_service.find_all())})
        return jsonify(response.build()), response.status_code
    except Exception as e:
        e = str(e)
        response.add_status_code(400).add_message('An error occurred while searching for the bookings!').add_data({"error": e})
        return jsonify(response.build()), response.status_code
    
@booking.route('/findbyid/<int:id>', methods=['GET'])
def find_by_id(id):
    try:
        response.add_status_code(200).add_message('Booking found!').add_data({"booking": booking_schema.dump(booking_service.find_by_id(id))})
        return jsonify(response.build()), response.status_code
    except Exception as e:
        e = str(e)
        response.add_status_code(400).add_message('An error occurred while searching for the booking!').add_data({"error": e})
        return jsonify(response.build()), response.status_code
    
@booking.route('/update/<int:id>', methods=['PUT'])
def update(id):
    try:
        booking = booking_schema.load(request.json)
        response.add_status_code(200).add_message('Booking updated!').add_data(
            {"booking updated": booking_schema.dump(booking_service.update(booking, id))}
        )
        return jsonify(response.build()), response.status_code
    except Exception as e:
        e = str(e)
        response.add_status_code(400).add_message('An error occurred while updating the booking!').add_data({"error": e})
        return jsonify(response.build()), response.status_code

