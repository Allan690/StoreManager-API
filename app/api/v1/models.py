import re


class User(object):
    """Store user data in dictionaries"""

    def __init__(self):
        self.users = {}

    def create_user(self, email, password, admin=False):
        """Creates a new user and appends them to the list of users"""
        data = {'id': len(self.users) + 1,
                'email': email,
                'password': password,
                'admin': admin}
        self.users[email] = data
        return self.users

    def get_all_users(self):
        """Gets all users in the users list"""
        return self.users

    def find_user_by_id(self, user_id):
        """finds a user in the list using his user id"""
        if self.users:
            for user in self.users.values():
                if user.get('id') == user_id:
                    return user

    @staticmethod
    def validate_email(email):
        """This method uses a regular expression to validate email entered by user"""
        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
            return True
        return False


class Product(object):
    """Stores product data in dictionaries"""

    def __init__(self):
        self.products = {}

    def create_product(self, name, description, price, category):
        """Adds a new  product to products dictionary"""
        new_prod = {'prod_id': len(self.products) + 1,
                    'name': name,
                    'description': description,
                    'price': price,
                    'category': category
                    }
        self.products[name] = new_prod
        return self.products

    def find_product_by_id(self, prod_id):
        """finds a product in the list using its product id"""
        if self.products:
            for product in self.products.values():
                if product.get('prod_id') == prod_id:
                    return product

    def update_product(self, prod_id, name, description, price):
        """Updates the name, description and price of a product"""
        if self.products:
            for product in self.products.values():
                if product.get('prod_id') == prod_id:
                    product['name'] = name
                    product['description'] = description
                    product['price'] = price
                    return product

    def get_all_products(self):
        """Returns the whole list of products"""
        return self.products


class Sales(object):
    """defines methods that store sales records in dictionaries"""

    def __init__(self):
        self.Sales = {}

    def create_sale(self, name, description, quantity, total):
        """Adds a new sales record to the Sales dictionary"""
        new_sale = {'sales_id': len(self.Sales) + 1,
                    'name': name,
                    'description': description,
                    'quantity': quantity,
                    'total': total
                    }
        self.Sales[name] = new_sale
        return self.Sales

    def find_sale_by_id(self, sales_id):
        """finds a sale record in the list using its sales id"""
        if self.Sales:
            for sales in self.Sales.values():
                if sales.get('sales_id') == sales_id:
                    return sales

    def update_sales(self, sales_id, name, description, quantity, total):
        """Updates the details of a sales record """
        if self.Sales:
            for sale in self.Sales.values():
                if sale.get('sales_id') == sales_id:
                    sale['name'] = name
                    sale['description'] = description
                    sale['quantity'] = quantity
                    sale['total'] = total
                    return sale

    def get_all_sales(self):
        """Returns the whole list of sales records"""
        return self.Sales
