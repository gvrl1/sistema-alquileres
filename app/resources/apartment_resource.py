from flask import jsonify, Blueprint, request
from ..services.apartment_service import ApartmentService
from ..mapping.apartment_schema import ApartmentSchema

apartment = Blueprint('apartment', __name__)

ps = ApartmentSchema(many=True) # Para devolver varios departamentos
apartment_schema = ApartmentSchema()
apartment_service = ApartmentService()

@apartment.route('/', methods=['GET'])
def index():
    resp = jsonify('OK this is Apartment resource')
    resp.status_code = 200
    return resp

@apartment.route('/create', methods=['POST'])
def create():
    try:
        apartment = apartment_schema.load(request.json)
        return {"apartment created": apartment_schema.dump(apartment_service.create(apartment))}, 200
    except Exception as e:
        e = str(e)
        return jsonify(f"{e}"), 400
    
@apartment.route('/update/<int:id>', methods=['POST'])
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
        return {"apartment": apartment_schema.dump(apartment_service.find_by_id(id))}, 200
    except Exception as e:
        e = str(e)
        return jsonify(e), 400
    
@apartment.route('/findall', methods=['GET'])
def find_all():
    try:
        return {"apartments": ps.dump(apartment_service.find_all())}, 200
    except Exception as e:
        e = str(e)
        return jsonify(e), 400
    
@apartment.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        return {"apartment deleted": apartment_schema.dump(apartment_service.delete(id))}, 200
    except Exception as e:
        e = str(e)
        return jsonify(e), 400