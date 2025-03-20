from flask import Blueprint, jsonify, request
from services.book_reservation import BookLendingService
from DAO.book_lending_dao import BookLendingDAO
from flask_jwt_extended import jwt_required, get_jwt_identity

book_lending_bp = Blueprint("book_lending", __name__)
book_lending = BookLendingDAO()

@book_lending_bp.route('/request_book', methods=['POST'])
@jwt_required()
def request_book():
    user_data = request.json
    return jsonify(BookLendingService.request_book(get_jwt_identity(), user_data["title"])), 200

@book_lending_bp.route("/return_book", methods=["POST"])
@jwt_required()
def return_book():
    user_data = request.json
    return book_lending.delete_lending(get_jwt_identity(), user_data["title"])