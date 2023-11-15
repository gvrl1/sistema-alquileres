from flask import Blueprint, jsonify, request
from app.services import UserService
from app.mapping import UserSchema
from app.dto import ResponseBuilder
from app.validators import validate_with

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
    response.add_status_code(200).add_message('Users found!').add_data({"Users": ps.dump(user_service.find_all())})
    return jsonify(response.build()), response.status_code
    

@user.route('/findbyid/<int:id>', methods=['GET'])
def find_by_id(id):
    response.add_status_code(200).add_message('User found!').add_data({"User": user_schema.dump(user_service.find_by_id(id))})
    return jsonify(response.build()), response.status_code
    
    
@user.route('/update/<int:id>', methods=['PUT'])
@validate_with(UserSchema)
def update(validated_data, id):
    user = validated_data
    response.add_status_code(200).add_message('User updated!').add_data(
        {"user updated": user_schema.dump(user_service.update(user, id))}
    )
    return jsonify(response.build()), response.status_code


@user.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    response.add_status_code(200).add_message('User deleted!').add_data({"User deleted": user_schema.dump(user_service.delete(id))})
    return jsonify(response.build()), response.status_code
