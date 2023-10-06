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

@user.route('/findbyid/<int:id>', methods=['GET'])
def find_by_id():
    # Devolver un cliente
    try:
        return {"user": user_schema.dump(user_service.find_by_id(id))}, 200
    except Exception as e:
        return jsonify(e), 400
    

@user.route('/create', methods=['POST'])
def create():
    # Crear un cliente
    try:
        user = user_schema.load(request.json)
        return {"user": user_schema.dump(user_service.create(user))}, 200
    except Exception as e:
        e = str(e)
        return jsonify(f"{e}"), 400