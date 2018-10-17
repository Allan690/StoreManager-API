from flask import request, jsonify, Blueprint
from app.api.v1.models import Product

product_obj = Product()
prod = Blueprint('v1_prod', __name__)


# this class contains methods which define the application routes
# noinspection PyMethodParameters
class ProductViews:

    @prod.route('/api/v1/products', methods=['POST'])
    def post_product():
        data = request.get_json()
        if not data or not data['name']:
            return jsonify({"Message": "Name is required!"}), 400
        elif not data['category']:
            return jsonify({"Message": "Category is required!"}), 400
        elif not data['description']:
            return jsonify({"Message": "Description is required!"}), 400

        if data['name'] in product_obj.products:
            return jsonify({"Message": "Name already exists!"}), 400
        product_obj.create_product(data['name'],
                                   data['description'],
                                   data['price'],
                                   data['category']
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
    def put_update_product(product_id):
        """Updates a product's details"""
        data = request.get_json()
        new_name = data['name']
        new_description = data['description']
        new_price = data['price']
        product = product_obj.find_product_by_id(product_id)
        if product:
            resp = product_obj.update_product(
                product_id, new_name, new_description, new_price
            )
            if resp:
                if new_name not in product_obj.products:
                    return jsonify({'Message': 'Product updated'}), 200
                return jsonify({'Message': 'Product name already exists'}), 400

        return jsonify({'Message': 'product not found'}), 404

    @prod.route('/api/v1/products', methods=['GET'])
    def get_all_products():
        return jsonify({"products": product_obj.products}), 200

    @prod.route('/api/v1/products/<int:product_id>', methods=['DELETE'])
    def remove_product(product_id):
        """Remove sale by id"""
        product = product_obj.find_product_by_id(product_id)
        if product:
                del product_obj.products[product['name']]
                return jsonify({"Message": "Product deleted successfully!"}), 200
        return jsonify({"Message": "Product not found"}), 404
