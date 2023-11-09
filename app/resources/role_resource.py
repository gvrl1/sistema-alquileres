from flask import jsonify, Blueprint, request
from ..services.role_service import RoleService
from ..mapping.role_schema import RoleSchema
from ..dto import ResponseBuilder

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
def create():
    try:
        role = role_schema.load(request.json) #load convierte de json a objeto Role
        response.add_status_code(200).add_message('Role created!').add_data(
            {"role created": role_schema.dump(role_service.create(role))}
        )
        return jsonify(response.build()), response.status_code
    except Exception as e:
        e = str(e)
        response.add_status_code(400).add_message('An error occurred while creating a role!').add_data({"error": e})
        return jsonify(response.build()), response.status_code

@role.route('/update/<int:id>', methods=['PUT'])
def update(id):
    try:
        role = role_schema.load(request.json)
        response.add_status_code(200).add_message('Role updated!').add_data(
            {"role updated": role_schema.dump(role_service.update(role, id))}
        )
        return jsonify(response.build()), response.status_code
    except Exception as e:
        e = str(e)
        response.add_status_code(400).add_message('An error occurred while updating a role!').add_data({"error": e})
        return jsonify(response.build()), response.status_code
    
@role.route('/findbyid/<int:id>', methods=['GET'])
def find_by_id(id):
    try:
        response.add_status_code(200).add_message('Role found!').add_data({"role": role_schema.dump(role_service.find_by_id(id))})
        return jsonify(response.build()), response.status_code
    except Exception as e:
        e = str(e)
        response.add_status_code(400).add_message('An error occurred while searching for the role!').add_data({"error": e})
        return jsonify(response.build()), response.status_code
    
@role.route('/findall', methods=['GET'])
def find_all():
    try:
        response.add_status_code(200).add_message('Roles found!').add_data({"roles": ps.dump(role_service.find_all())})
        return jsonify(response.build()), response.status_code
    except Exception as e:
        e = str(e)
        response.add_status_code(400).add_message('An error occurred while searching for the roles!').add_data({"error": e})
        return jsonify(response.build()), response.status_code
    
@role.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        response.add_status_code(200).add_message('Role deleted!').add_data({"role deleted": role_schema.dump(role_service.delete(id))})
        return jsonify(response.build()), response.status_code
    except Exception as e:
        e = str(e)
        response.add_status_code(400).add_message('An error occurred while deleting the role!').add_data({"error": e})
        return jsonify(response.build()), response.status_code
