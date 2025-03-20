from database import db
from models import Account, Address
import logging
from flask import jsonify
from flask_jwt_extended import create_access_token
from datetime import timedelta
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()
logger = logging.getLogger(__name__) 


class UserDAO:
    
    @staticmethod
    def check_username_exists(username):
        print("debug")
        return db.session.query(Account).filter_by(username=username).first() is not None
    
    @staticmethod
    def register_user(username, password, email, street_address, city, state, country, phone):
         
        if not UserDAO.check_username_exists(username):
            
            password = bcrypt.generate_password_hash(password=password).decode('utf-8')
            address = Address(
                street_address=street_address,
                city=city,
                state=state,
                country=country,
                phone=phone
            )

            account = Account(
                username=username,
                email=email,
                password=password,
                address=address
            )
    
            db.session.add(account)
            db.session.commit()
            return jsonify({"Info": "username created succefully"})
        else:
            logger.error("Username name already exsists.")
            return jsonify({"error": "Username name already exsists."})

    @staticmethod
    def login(username, password):
        
        user = db.session.query(Account).filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            access_token = create_access_token(identity=username, expires_delta=timedelta(minutes=10))
            return jsonify({"access_token": access_token}), 200

        return jsonify({"error": "Invalid credentials"}), 401
    
    @staticmethod
    def get_account_id_by_username(username):
        account = db.session.query(Account.account_id).filter_by(username=username).first()
        return account.account_id if account else None
