from flask import Blueprint, jsonify, request
from ..services.user_service import UserService
from ..mapping.user_schema import UserSchema
from ..dto import ResponseBuilder

ps = UserSchema(many=True) # Para devolver varios usuarios
user = Blueprint('user', __name__)

user_schema = UserSchema() # Para devolver un usuario
user_service = UserService()
response = ResponseBuilder()

@user.route('/', methods=['GET'])
def index():
    response.add_status_code(200).add_message('OK this is User resource').add_data({"message": "OK this is User resource"})
    return jsonify(response.build()), response.status_code


@user.route('/findall', methods=['GET'])
def find_all():
    try:
        response.add_status_code(200).add_message('Users found!').add_data({"Users": ps.dump(user_service.find_all())})
        return jsonify(response.build()), response.status_code
    except Exception as e:
        e = str(e)
        response.add_status_code(400).add_message('An error occurred while searching for the users!').add_data({"error": e})
        return jsonify(response.build()), response.status_code

@user.route('/findbyid/<int:id>', methods=['GET'])
def find_by_id(id):
    try:
        response.add_status_code(200).add_message('User found!').add_data({"User": user_schema.dump(user_service.find_by_id(id))})
        return jsonify(response.build()), response.status_code
    except Exception as e:
        e = str(e)
        response.add_status_code(400).add_message('An error occurred while searching for the user!').add_data({"error": e})
        return jsonify(response.build()), response.status_code
    
@user.route('/update/<int:id>', methods=['PUT'])
def update(id):
    try:
        user = user_schema.load(request.json)
        response.add_status_code(200).add_message('User updated!').add_data(
            {"user updated": user_schema.dump(user_service.update(user, id))}
        )
        return jsonify(response.build()), response.status_code
    except Exception as e:
        e = str(e)
        response.add_status_code(400).add_message('An error occurred while updating the user!').add_data({"error": e})
        return jsonify(response.build()), response.status_code

@user.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        response.add_status_code(200).add_message('User deleted!').add_data({"User deleted": user_schema.dump(user_service.delete(id))})
        return jsonify(response.build()), response.status_code
    except Exception as e:
        e = str(e)
        response.add_status_code(400).add_message('An error occurred while deleting the user!').add_data({"error": e})
        return jsonify(response.build()), response.status_code
