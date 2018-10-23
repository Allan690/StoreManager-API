from app.api.v1.views.user_view import login_token
from flask import request, jsonify, Blueprint
from app.api.v1.models import Sales

sales_obj = Sales()
sal = Blueprint('v1_sal', __name__)


# this class contains methods which define the application routes
# noinspection PyMethodParameters
class SalesViews(object):
    def __init__(self, current_user):
        self.current_user = current_user

    def __getitem__(self, item):
        return self.current_user[item]

    @sal.route('/api/v1/sales', methods=['POST'])
    @login_token
    def post_new_sale_record(current_user):
        data = request.get_json()
        if not data or not data['name']:
            return jsonify({"Message": "Name is required!"}), 400
        elif not data['quantity'] or data['quantity'] == 0:
            return jsonify({"Message": "Quantity is required!"}), 400
        elif not data['description']:
            return jsonify({"Message": "Description is required!"}), 400
        elif not data['total']:
            return jsonify({"Message": "Total is required!"}), 400

        if data['name'] in sales_obj.Sales:
            return jsonify({"Message": "Name already exists!"}), 400
        user_id = current_user['email']
        sales_obj.create_sale(data['name'],
                              data['quantity'],
                              data['description'],
                              data['total'], user_id
                              )
        return jsonify({"Message": "Sale registered successfully"}), 201

    @sal.route('/api/v1/sales/<int:sales_id>', methods=['GET'])
    def get_one_sale(sales_id):
        """Returns a single sale record"""
        response = sales_obj.find_sale_by_id(sales_id)
        if response:
            return jsonify({"Sales Profile": response}), 200
        return jsonify({"Message": "Sale not found"}), 404

    @sal.route('/api/v1/sales/<int:sales_id>', methods=['PUT'])
    @login_token
    def put_update_sale(current_user, sales_id):
        """Updates a sale's details"""
        data = request.get_json()
        new_name = data['name']
        new_quantity = data['quantity']
        new_description = data['description']
        new_total = data['total']
        sale = sales_obj.find_sale_by_id(sales_id)
        if sale:
            if current_user['email'] == sale['user_id']:
                resp = sales_obj.update_sales(
                    sales_id, new_name, new_quantity, new_description, new_total
                )
                if resp:
                    if new_name not in sales_obj.Sales:
                        return jsonify({'Message': 'Sale updated'}), 200
                    return jsonify({'Message': 'Sale name already exists'}), 400

        return jsonify({'Message': 'sale not found'}), 404

    @sal.route('/api/v1/sales', methods=['GET'])
    def get_all_sales():
        return jsonify({"sales": sales_obj.Sales}), 200

    @sal.route('/api/v1/sales/<int:sales_id>', methods=['DELETE'])
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
