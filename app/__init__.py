from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from app.config.database import db, FULL_URL_DB


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    migrate = Migrate()
    migrate.init_app(app, db)

    return app