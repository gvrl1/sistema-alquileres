from flask import Blueprint, jsonify, request
from ..services.user_service import UserService
from ..mapping.user_schema import UserSchema

ps = UserSchema(many=True) # Para devolver varios usuarios
user = Blueprint('user', __name__)

user_schema = UserSchema() # Para devolver un usuario
user_service = UserService()

# @user.route('/', methods=['GET'])
# def index():
#     # Devolver todos los clientes
#     resp = jsonify('OK CLIENTE')
#     resp.status_code = 200
#     return resp

# @user.route('/findall', methods=['GET'])
# def find_all():
#     # Devolver todos los clientes
#     
#     resp = jsonify(service.find_all())
#     resp.status_code = 200
#     return jsonify(resp)

# @user.route('/<int:id>', methods=['GET'])
# def find_id():
#     # Devolver un cliente
#     
#     return

@user.route('/singup', methods=['POST'])
def singup():
    # Crear un cliente
    try:
        data = request.get_json()
        user = user_schema.load(data)
        user = user_service.create(user)
        return user_schema.dump(user), 201
    except Exception as e:
        return jsonify(e), 400