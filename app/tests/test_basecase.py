import unittest
from app import flaskApp
from app.api.v1.models import Product
from app.api.v1.models import Sales


class TestSetUp(unittest.TestCase):
    """Initialize the app with test data"""

    def setUp(self):
        self.app = flaskApp.test_client()
        self.user = dict(email="testuser@gmail.com", password="testpass")
        self.un_known_user = dict(email="username@gmail.com", password="password")
        self.product = dict(name="Shoe Polish", description="Kiwi Shoe Polish", price="50", category="accessories")
        self.new_product = dict(name="Kiatu mzuri", description="Ni kiatu tu", price="1200",
                                category="footware")
        self.empty_product = dict(name="", description="", price="", category="")
        self.missing_prod_category = dict(name="Shoe", description="Ni kiatu tu", price="1200",
                                          category="")
        self.missing_prod_description = dict(name="Kiatu mzuri", description="", price="1200",
                                             category="footware")
        self.missing_prod_price = dict(name="Kiatu mzuri", description="", price="",
                                       category="footware")
        self.new_product = dict(name="Kiatu mzuri", description="Ni kiatu tu", price="1200",
                                category="footware")
        self.sale = dict(name="Shoes", description="All kinds of shoes", quantity="50", total="10000")
        self.new_sale = dict(name="Spoons", description="Ni vijiko jamani", quantity="120", total="3000")
        self.empty_sale = dict(name="", description="", price="", category="")
        self.missing_sale_quantity = dict(name="Spoons", description="Ni vijiko jamani", quantity="", total="3000")
        self.missing_sale_description = dict(name="Spoons", description="", quantity="120", total="3000")
        self.missing_sale_total = dict(name="Spoons", description="Ni vijiko jamani", quantity="120", total="")

    def tearDown(self):
        """destroys the test data after completion of tests"""
        Product.products = []
        Sales.Sales = []