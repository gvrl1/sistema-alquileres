from flask import jsonify, Blueprint, request
from ..services.role_service import RoleService
from ..mapping.role_schema import RoleSchema

role = Blueprint('role', __name__)

ps = RoleSchema(many=True) # Para devolver varios roles
role_schema = RoleSchema()
role_service = RoleService()

@role.route('/', methods=['GET'])
def index():
    resp = jsonify('OK this is Role resource')
    resp.status_code = 200
    return resp

@role.route('/create', methods=['POST'])
def create():
    try:
        role = role_schema.load(request.json) #load convierte de json a objeto Role
        return {"role created": role_schema.dump(role_service.create(role))}, 200 #dump convierte de objeto a json
    except Exception as e:
        e = str(e)
        return jsonify(f"{e}"), 400

@role.route('/update/<int:id>', methods=['PUT'])
def update(id):
    try:
        role = role_schema.load(request.json)
        return {"role updated": role_schema.dump(role_service.update(role, id))}, 200
    except Exception as e:
        e = str(e)
        return jsonify(f"{e}"), 400
    
@role.route('/findbyid/<int:id>', methods=['GET'])
def find_by_id(id):
    try:
        return {"role": role_schema.dump(role_service.find_by_id(id))}, 200
    except Exception as e:
        e = str(e)
        return jsonify(e), 400
    
@role.route('/findall', methods=['GET'])
def find_all():
    try:
        return {"roles": ps.dump(role_service.find_all())}, 200
    except Exception as e:
        e = str(e)
        return jsonify(e), 400
    
@role.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        return {"role deleted": role_schema.dump(role_service.delete(id))}, 200
    except Exception as e:
        e = str(e)
        return jsonify(e), 400