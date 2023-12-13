from flask import jsonify, Blueprint, request
from app.services.role_service import RoleService
from app.mapping.role_schema import RoleSchema
from app.dto import ResponseBuilder
from app.validators import validate_with, validate_exists

role = Blueprint('role', __name__)

ps = RoleSchema(many=True) # Para devolver varios roles
role_schema = RoleSchema()
role_service = RoleService()
response = ResponseBuilder()

@role.route('/', methods=['GET'])
def index():
    response.add_status_code(200).add_message('OK this is Role resource').add_data({"message": "OK this is Role resource"})
    return jsonify(response.build()), response.status_code

@role.route('/create', methods=['POST'])
@validate_with(RoleSchema)
def create(validated_data):
    role = validated_data
    response.add_status_code(200).add_message('Role created!').add_data(
        {"role created": role_schema.dump(role_service.create(role))}
    )
    return jsonify(response.build()), response.status_code
    

@role.route('/update/<int:id>', methods=['PUT'])
@validate_with(RoleSchema)
@validate_exists(role_service, response)
def update(validated_data, id):
    role = validated_data
    response.add_status_code(200).add_message('Role updated!').add_data(
        {"role updated": role_schema.dump(role_service.update(role, id))}
    )
    return jsonify(response.build()), response.status_code
    
    
@role.route('/findbyid/<int:id>', methods=['GET'])
@validate_exists(role_service, response)
def find_by_id(id):
    response.add_status_code(200).add_message('Role found!').add_data({"role": role_schema.dump(role_service.find_by_id(id))})
    return jsonify(response.build()), response.status_code
    
    
@role.route('/findall', methods=['GET'])
def find_all():
    if not role_service.find_all():
        response.add_status_code(400).add_message('There are no roles created!').add_data()
        return jsonify(response.build()), response.status_code
    response.add_status_code(200).add_message('Roles found!').add_data({"roles": ps.dump(role_service.find_all())})
    return jsonify(response.build()), response.status_code
    
    
@role.route('/delete/<int:id>', methods=['DELETE'])
@validate_exists(role_service, response)
def delete(id):
    response.add_status_code(200).add_message('Role deleted!').add_data({"role deleted": role_schema.dump(role_service.delete(id))})
    return jsonify(response.build()), response.status_code
