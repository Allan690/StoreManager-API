class Product(object):
    """Stores product data in dictionaries"""

    def __init__(self):
        self.products = {}

    def create_product(self, name, description, price, quantity, user_id):
        """Adds a new  product to products dictionary"""
        new_prod = {'prod_id': len(self.products) + 1,
                    'name': name,
                    'description': description,
                    'price': price,
                    'quantity': quantity,
                    'user_id': user_id
                    }
        self.products[name] = new_prod
        return self.products

    def find_product_by_id(self, prod_id):
        """finds a product in the list using its product id"""
        if self.products:
            for product in self.products.values():
                if product.get('prod_id') == prod_id:
                    return product

    def find_product_by_name(self, prod_name):
        if self.products:
            for self.product_item in self.products.values():
                if self.product_item['name'] == prod_name:
                    return self.product_item

    def update_product(self, prod_id, name, description, price, quantity):
        """Updates the name, description and price of a product"""
        if self.products:
            for product in self.products.values():
                if product.get('prod_id') == prod_id:
                    product['name'] = name
                    product['description'] = description
                    product['price'] = price
                    product['quantity'] = quantity
                    return product

    def get_all_products(self):
        """Returns the whole list of products"""
        return self.products

