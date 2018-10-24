from .product_models import Product


class Sales(object):
    """defines methods that store sales records in dictionaries"""
    prod = Product()

    def __init__(self):
        self.Sales = {}

    def create_sale(self, name, description, quantity, total, user_id):
        """Adds a new sales record to the Sales dictionary"""

        new_sale = {'sales_id': len(self.Sales) + 1,
                    'name': name,
                    'description': description,
                    'quantity': quantity,
                    'total': total,
                    'user_id': user_id
                    }
        if self.prod.products:
            for prod in self.prod.products.values():
                if prod.get('name') == name:
                    prod['quantity'] = prod['quantity'] - quantity
                    return prod
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

