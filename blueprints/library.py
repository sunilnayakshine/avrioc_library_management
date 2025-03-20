from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from DAO.book_dao import BookDAO
from services.libray_management import LibraryService
from database import db
from models import Librarian, Account
import functools


library_bp = Blueprint("library", __name__)

def is_librarian(username):
    """Check if the given username belongs to a librarian."""
    account = db.session.query(Account).filter_by(username=username).first()
    
    if not account:
        return False  # User not found
    
    librarian = db.session.query(Librarian).filter_by(account_id=account.account_id).first()
    return librarian is not None  # True if librarian, False otherwise

def role_required(required_role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            
            if required_role == "librarian" and not is_librarian(get_jwt_identity()):
                return jsonify({"error": "Unauthorized access"}), 403

            return func(*args, **kwargs)
        return wrapper
    return decorator

@library_bp.route("/add_category", methods=["POST"])
@jwt_required()
@role_required("librarian")
def add_category():
    user_data = request.json
    return LibraryService.add_category(user_data["category"])

@library_bp.route("/add_book", methods=["POST"])
@jwt_required()
@role_required("librarian")
def add_book():
    user_data = request.json
    return LibraryService.add_book(**user_data)

@library_bp.route("/update_book", methods=["POST"])
@jwt_required()
@role_required("librarian")
def update_book():
    user_data = request.json
    return LibraryService.update_book(**user_data)

@library_bp.route("/delete_book", methods=["POST"])
@jwt_required()
@role_required("librarian")
def delete_book():
    user_data = request.json
    return LibraryService.delete_book(user_data["isbn"])