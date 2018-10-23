from app.api.v1.views.user_view import login_token
from flask import request, jsonify, Blueprint
from app.api.v1.models import Product

product_obj = Product()
prod = Blueprint('v1_prod', __name__)


# this class contains methods which define the application routes
# noinspection PyMethodParameters
class ProductViews(object):
    def __init__(self, current_user):
        self.current_user = current_user

    def __getitem__(self, item):
        return self.current_user[item]

    @prod.route('/api/v1/products', methods=['POST'])
    @login_token
    def post_product(current_user):
        data = request.get_json()
        if not data or not data['name']:
            return jsonify({"Message": "Name is required!"}), 400
        elif not data['quantity']:
            return jsonify({"Message": "Quantity is required!"}), 400
        elif not data['description']:
            return jsonify({"Message": "Description is required!"}), 400

        if data['name'] in product_obj.products:
            return jsonify({"Message": "Name already exists!"}), 400
        user_id = current_user['email']
        product_obj.create_product(data['name'],
                                   data['description'],
                                   data['price'],
                                   data['quantity'], user_id
                                   )
        return jsonify({"Message": "Product registered successfully"}), 201

    @prod.route('/api/v1/products/<int:product_id>', methods=['GET'])
    def get_one_prod(product_id):
        """Returns a single product"""
        response = product_obj.find_product_by_id(product_id)
        if response:
            return jsonify({"Product Profile": response}), 200
        return jsonify({"Message": "Product not found"}), 404

    @prod.route('/api/v1/products/<int:product_id>', methods=['PUT'])
    @login_token
    def put_update_product(current_user, product_id):
        """Updates a product's details"""
        data = request.get_json()
        new_name = data['name']
        new_description = data['description']
        new_price = data['price']
        new_quantity = data['quantity']
        product = product_obj.find_product_by_id(product_id)
        if product:
            if current_user['email'] == product['user_id']:
                resp = product_obj.update_product(
                    product_id, new_name, new_description, new_price, new_quantity
                )
                if resp:
                    if new_name not in product_obj.products:
                        return jsonify({'Message': 'Product updated'}), 200
                    return jsonify({'Message': 'Product name already exists'}), 400
            return jsonify({"Message": "Unauthorized:You can only update a product if admin!!"}), 401

        return jsonify({'Message': 'product not found'}), 404

    @prod.route('/api/v1/products', methods=['GET'])
    def get_all_products():
        """View all available products"""
        return jsonify({"products": product_obj.products}), 200

    @prod.route('/api/v1/products/<int:product_id>', methods=['DELETE'])
    @login_token
    def remove_product(current_user, product_id):
        """Remove product by id"""
        product = product_obj.find_product_by_id(product_id)
        if product:
            if current_user['email'] == product['user_id']:
                del product_obj.products[product['name']]
                return jsonify({"Message": "Product deleted successfully!"}), 200
            return jsonify({"Message": "Unauthorized: Only admin can delete a product!!"}), 401
        return jsonify({"Message": "Product not found"}), 404
