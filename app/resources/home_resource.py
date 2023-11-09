from flask import jsonify, Blueprint
from app.dto import ResponseBuilder

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def index():
    response = ResponseBuilder()
    response.add_status_code(200).add_message('Hello World!').add_data({"Home":"/home"})
    return jsonify(response.build()), 200
