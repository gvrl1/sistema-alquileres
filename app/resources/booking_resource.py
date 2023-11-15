from flask import Blueprint, jsonify, request
from app.services.booking_service import BookingService
from app.mapping.booking_schema import BookingSchema
from app.dto import ResponseBuilder
from app.validators import validate_with

ps = BookingSchema(many=True) # Para devolver varios departamentos

booking = Blueprint('booking', __name__)

booking_schema = BookingSchema() # Para devolver una reserva
booking_service = BookingService()
response = ResponseBuilder()


@booking.route('/create', methods=['POST'])
@validate_with(BookingSchema)
def create(validated_data):
    booking = validated_data
    user_id = request.args.get('user_id')
    apartment_id = request.args.get('apartment_id')
    response.add_status_code(200).add_message('Booking created!').add_data(
        {"booking created": booking_schema.dump(booking_service.create(booking, user_id, apartment_id))}
    )
    return jsonify(response.build()), response.status_code
    
    
@booking.route('/findall', methods=['GET'])
def find_all():
    response.add_status_code(200).add_message('Bookings found!').add_data({"bookings": ps.dump(booking_service.find_all())})
    return jsonify(response.build()), response.status_code
    
    
@booking.route('/findbyid/<int:id>', methods=['GET'])
def find_by_id(id):
    response.add_status_code(200).add_message('Booking found!').add_data({"booking": booking_schema.dump(booking_service.find_by_id(id))})
    return jsonify(response.build()), response.status_code
    
    
@booking.route('/update/<int:id>', methods=['PUT'])
@validate_with(BookingSchema)
def update(validated_data, id):
    booking = validated_data
    response.add_status_code(200).add_message('Booking updated!').add_data(
        {"booking updated": booking_schema.dump(booking_service.update(booking, id))}
    )
    return jsonify(response.build()), response.status_code
