from flask import request, jsonify, Blueprint
from werkzeug.security import generate_password_hash
from app.api.v1.models import User

user_object = User()
user_dec = Blueprint('v1_user', __name__)  # authentication not enforced


# user views implemented without authentication
# noinspection PyMethodParameters
class UserViews:
    """This class contains the routes for the user endpoint"""
    """User can for now only register, reset password, get all users and search a user by id"""

    @user_dec.route('/api/v1/register', methods=['POST'])
    def create_user():
        """receive user input as json object"""
        data = request.get_json()
        password_hash = generate_password_hash(data['password'], method='sha256')
        validate_email = User.validate_email(data['email'])
        if data['email'] in user_object.users:
            return jsonify({'Message': "User already exists"}), 400
        if data['email'] == "" or data['password'] == "":
            return jsonify({'Message': "Email and Password is required"}), 400
        if validate_email:
            return jsonify({"Message": "Wrong email format: Enter a valid email address"}), 400
        user_object.create_user(data['email'], password_hash)
        return jsonify({"Message": "User registered successfully"}), 201

    @user_dec.route('/api/v1/reset-password', methods=['PUT'])
    def reset_password():
        """
        User can reset their password
        """
        data = request.get_json()
        password_hash = generate_password_hash(data['password'], method='sha256')
        usr = user_object.users[["email"]]
        usr.update({"password": password_hash})
        return jsonify({"Message": "password updated"}), 202

    @user_dec.route('/api/v1/users', methods=['GET'])
    def get_all_users():
        return jsonify({"users": user_object.users}), 200

    @user_dec.route('/api/v1/users/<int:user_id>', methods=['GET'])
    def get_user_by_id(user_id):
        response = user_object.find_user_by_id(user_id)
        if response:
            return jsonify({"User Profile": response}), 200
        return jsonify({"Message": "User not found"}), 404
