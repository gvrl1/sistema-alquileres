from flask import jsonify, Blueprint, request
from ..dto import ResponseBuilder
from ..mapping import UserSchema
from ..services import AuthService

auth = Blueprint('auth', __name__)
user_schema = UserSchema()
auth_service = AuthService()
response = ResponseBuilder()

@auth.route('/register', methods=['POST'])
def register():
    user = user_schema.load(request.json)
    register = auth_service.register(user)
    if not register:
        response.add_data(user_schema.dump(user)).add_message('Error de registro. Ya existe un usuario con ese email.').add_status_code(400)
        return jsonify(response.build()), response.status_code
    else:
        response.add_data(user_schema.dump(register)).add_message('Usuario registrado con éxito.').add_status_code(200)
        return jsonify(response.build()), response.status_code

@auth.route('/login', methods=['POST'])
def login():
    pass