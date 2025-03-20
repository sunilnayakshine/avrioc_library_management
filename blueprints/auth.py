from flask import Blueprint, request
from DAO.user_dao import UserDAO

auth_bp = Blueprint("auth", __name__)
user = UserDAO()


@auth_bp.route("/register", methods=["POST"])
def register():
    user_data = request.json
    return user.register_user(**user_data)


@auth_bp.route('/login', methods=['POST'])
def login():
    user_data = request.json
    return user.login(user_data["username"], user_data["password"])
