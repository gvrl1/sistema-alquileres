from flask import jsonify, Blueprint, request
from ..services.apartment_service import ApartmentService
from ..mapping.apartment_schema import ApartmentSchema
from ..dto import ResponseBuilder

apartment = Blueprint('apartment', __name__)

ps = ApartmentSchema(many=True) # Para devolver varios departamentos
apartment_schema = ApartmentSchema()
apartment_service = ApartmentService()
response = ResponseBuilder()

@apartment.route('/', methods=['GET'])
def index():
    response.add_status_code(200).add_message('This is apartment resource!').add_data()
    return jsonify(response.build()), response.status_code

@apartment.route('/create', methods=['POST'])
def create():
    try:
        apartment = apartment_schema.load(request.json)
        response.add_status_code(200).add_message('Apartment created!').add_data(
            {"apartment created": apartment_schema.dump(apartment_service.create(apartment))}
        )
        return jsonify(response.build()), response.status_code
    except Exception as e:
        e = str(e)
        response.add_status_code(400).add_message('An error occurred while creating a department!').add_data({"error": e})
        return jsonify(response.build()), response.status_code
    
@apartment.route('/update/<int:id>', methods=['PUT'])
def update(id):
    try:
        apartment = apartment_schema.load(request.json)
        return {"apartment updated": apartment_schema.dump(apartment_service.update(apartment, id))}, 200
    except Exception as e:
        e = str(e)
        return jsonify(f"{e}"), 400
    
@apartment.route('/findbyid/<int:id>', methods=['GET'])
def find_by_id(id):
    try:
        response.add_status_code(200).add_message('Apartment found!').add_data({"apartment": apartment_schema.dump(apartment_service.find_by_id(id))})
        return jsonify(response.build()), response.status_code
    except Exception as e:
        e = str(e)
        response.add_status_code(400).add_message('An error occurred while searching for the apartment!').add_data({"error": e})
        return jsonify(response.build()), response.status_code
    
@apartment.route('/findall', methods=['GET'])
def find_all():
    try:
        response.add_status_code(200).add_message('Apartments found!').add_data({"apartments": ps.dump(apartment_service.find_all())})
        return jsonify(response.build()), response.status_code
    except Exception as e:
        e = str(e)
        response.add_status_code(400).add_message('An error occurred while searching for the apartments!').add_data({"error": e})
        return jsonify(response.build()), response.status_code
    
@apartment.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        response.add_status_code(200).add_message('Apartment deleted!').add_data({"apartment deleted": apartment_schema.dump(apartment_service.delete(id))})
        return jsonify(response.build()), response.status_code
    except Exception as e:
        e = str(e)
        response.add_status_code(400).add_message('An error occurred while deleting the apartment!').add_data({"error": e})
        return jsonify(response.build()), response.status_code
    
@apartment.route('/search', methods=['GET'])
def search():
    try:
        lease_min = request.args.get('lease_min')
        lease_max = request.args.get('lease_max')
        response.add_status_code(200).add_message('Apartment found!').add_data({"apartments": ps.dump(apartment_service.search(lease_min, lease_max))})
        return jsonify(response.build()), response.status_code
    except Exception as e:
        e = str(e)
        response.add_status_code(400).add_message('An error occurred while searching for the apartment!').add_data({"error": e})
        return jsonify(response.build()), response.status_code