from flask import jsonify
from app.api.v1.models.user_models import User
from app.api.v1.models.sale_models import Sales
from app.api.v1.models.product_models import Product
user_object = User()
sales_obj = Sales()
prod_obj = Product()


def validate_user(data):
    validate_email = User.validate_email(data['email'])
    if data['email'] == "" or data['password'] == "":
        return jsonify({'Message': "Both email and password are required"}), 400
    for x in data['password']:
        if x.isspace():
            return jsonify({"Message": "Password can't contain spaces"}), 400
    if len(data['password'].strip()) < 8:
        return jsonify({"Message": "Password should have at least 8 characters"}), 400
    if validate_email:
        return jsonify({"Message": "Wrong email format: Enter a valid email address"}), 400


def validate_product(data):
    if not data or not data['name']:
        return jsonify({"Message": "Name is required!"}), 400
    elif not data['quantity'] or data['quantity'] == 0:
        return jsonify({"Message": "Quantity is required!"}), 400
    elif not data['description']:
        return jsonify({"Message": "Description is required!"}), 400
    if not isinstance(data['description'], str):
        return jsonify({"Message": "Description must be a string!"}), 400
    if not isinstance(data['name'], str):
        return jsonify({"Message": "Product name must be a string!"}), 400
    elif not data['price'] or data['price'] == 0:
        return jsonify({"Message": "Price is required!"}), 400
    if not isinstance(data['quantity'], int):
        return jsonify({"Message": "Quantity must be a number!"}), 400
    if not isinstance(data['price'], int):
        return jsonify({"Message": "Price must be a number!"}), 400


def validate_sales(data):
    if not data or not data['prod_id']:
        return jsonify({"Message": "Product ID is required!"}), 400
    if not isinstance(data['prod_id'], int):
        return jsonify({"Message": "Product ID must be a number!"}), 400
    elif not data['quantity'] or data['quantity'] == 0:
        return jsonify({"Message": "Quantity is required!"}), 400
    if not isinstance(data['quantity'], int):
        return jsonify({"Message": "Quantity must be a number!"}), 400
    if data['prod_id'] == 0:
        return jsonify({"Message": "Product ID cannot be 0!"}), 400


def validate_login(auth):
    if not auth:
        return jsonify({"Message": "Email and password required!"}), 401
    if not auth['email']:
        return jsonify({"Message": "Email is required"}), 401
    if not auth['password']:
        return jsonify({"Message": "password is required"}), 401




