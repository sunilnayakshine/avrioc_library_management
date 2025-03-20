
from flask import Blueprint, request, jsonify
from services.book import BookService
from flask_jwt_extended import jwt_required

book_bp = Blueprint("book", __name__)

@book_bp.route("/books", methods=["POST"])
@jwt_required()
def get_books():
    user_data = request.json or {}
    
    title = user_data.get("title")
    category_name = user_data.get("category_name")
    publisher = user_data.get("publisher")

    books = BookService.fetch_books(title=title, category_name=category_name, publisher=publisher)
    
    return jsonify(books), 200 if books else 404

