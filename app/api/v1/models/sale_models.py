from .product_models import Product
prod_obj = Product()


class Sales(object):
    """defines methods that store sales records in dictionaries"""
    def __init__(self):
        self.Sales = {}

    def create_sale(self, name, description, quantity, price,  prod_id, user_id):
        """Adds a new sales record to the Sales dictionary"""

        new_sale = {'sales_id': len(self.Sales) + 1,
                    'name': name,
                    'description': description,
                    'quantity': quantity,
                    'price': price,
                    'user_id': user_id,
                    'prod_id': prod_id,
                    'total': quantity * price
                    }
        self.Sales[name] = new_sale
        return self.Sales

    def find_sale_by_id(self, sales_id):
        """finds a sale record in the list using its sales id"""
        if self.Sales:
            for sales in self.Sales.values():
                if sales.get('sales_id') == sales_id:
                    return sales

    def update_sales(self, sales_id, name, description, total):
        """Updates the details of a sales record """
        if self.Sales:
            for sale in self.Sales.values():
                if sale.get('sales_id') == sales_id:
                    sale['name'] = name
                    sale['description'] = description
                    sale['total'] = total
                    return sale

    def get_all_sales(self):
        """Returns the whole list of sales records"""
        return self.Sales












































