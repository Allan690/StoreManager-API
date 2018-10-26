from app.api.v1.views.user_view import login_token
from flask import request, jsonify, Blueprint
from app.api.v1.models.product_models import Product
from app.api.v1.models.sale_models import Sales
from app.api.v1.utils import validate_product, validate_sales
product_obj = Product()
sales_obj = Sales()
prod = Blueprint('v1_prod', __name__)


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
        if data['name'] in product_obj.products:
            return jsonify({"Message": "Name already exists!"}), 400
        if validate_product(data):
            return validate_product(data)

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

    @prod.route('/api/v1/sales', methods=['POST'])
    @login_token
    def post_new_sale_record(current_user):
        data = request.get_json()
        prod_id = data['prod_id']
        user_id = current_user['email']
        if validate_sales(data):
            return validate_sales(data)
        if product_obj.find_product_by_id(prod_id):
            prod_on_sale = product_obj.find_product_by_id(prod_id)
            if data['quantity'] < prod_on_sale["quantity"]:
                resp = sales_obj.create_sale(prod_on_sale['name'],
                                             prod_on_sale['description'],
                                             data['quantity'],
                                             prod_on_sale['price'],
                                             data['prod_id'],
                                             user_id
                                      )
                product_obj.update_product(prod_id, prod_on_sale['name'], prod_on_sale['description'],
                                                  prod_on_sale['price'], prod_on_sale['quantity'] - data['quantity']
                                               )
                return jsonify({"Sale record": resp,
                                "Message":
                                    f"Sale Created successfully."
                                    f" {data['quantity']} units of {prod_on_sale['name']} sold. "
                                    f"The quantity of product has been updated."}
                               ), 201

            return jsonify({"Message": f"The quantity you entered exceeds stocked quantity"}), 400
        return jsonify({"Message": f"product does not exist"}), 404

    @prod.route('/api/v1/sales/<int:sales_id>', methods=['GET'])
    def get_one_sale(sales_id):
        """Returns a single sale record"""
        response = sales_obj.find_sale_by_id(sales_id)
        if response:
            return jsonify({"Sales Profile": response}), 200
        return jsonify({"Message": "Sale not found"}), 404

    @prod.route('/api/v1/sales', methods=['GET'])
    def get_all_sales():
        return jsonify({"sales": sales_obj.Sales}), 200

    @prod.route('/api/v1/sales/<int:sales_id>', methods=['PUT'])
    @login_token
    def put_update_sale(current_user, sales_id):
        """Updates a sale's details"""
        data = request.get_json()
        new_name = data['name']
        new_description = data['description']
        new_total = data['total']
        sale = sales_obj.find_sale_by_id(sales_id)
        if sale:
            if current_user['email'] == sale['user_id']:
                resp = sales_obj.update_sales(
                    sales_id, new_name, new_description, new_total
                )
                if resp:
                    if new_name not in sales_obj.Sales:
                        return jsonify({'Message': 'Sale updated'}), 200
                    return jsonify({'Message': 'Sale name already exists'}), 400
        return jsonify({'Message': 'Sale not found'}), 404

    @prod.route('/api/v1/sales/<int:sales_id>', methods=['DELETE'])
    @login_token
    def remove_sale(current_user, sales_id):
        """Remove sale record by id"""
        sale = sales_obj.find_sale_by_id(sales_id)
        if sale:
            if current_user['email'] == sale['user_id']:
                del sales_obj.Sales[sale['name']]
                return jsonify({"Message": "Sale deleted successfully!"}), 200
            return jsonify({"Message": "Unauthorized: Sale deletion unauthorized!!"}), 401
        return jsonify({"Message": "Sale not found"}), 404
