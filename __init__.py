from flask import Flask
from flask_jwt_extended import JWTManager
from database import db
from blueprints.auth import auth_bp
from blueprints.book_lending import book_lending_bp
from blueprints.library import library_bp
from blueprints.book import book_bp
from config import config

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = config.SECRET_KEY
    app.config["JWT_SECRET_KEY"] = config.JWT_SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
    
    db.init_app(app)
    JWTManager(app)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(book_lending_bp, url_prefix="/book_lending")
    app.register_blueprint(library_bp, url_prefix="/library")
    app.register_blueprint(book_bp, url_prefix="/book")

    return app