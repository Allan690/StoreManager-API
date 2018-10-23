import unittest
import json
from app import flask_app


class TestSetUp(unittest.TestCase):
    """Initialize the app with test data"""
    def setUp(self):
        self.app = flask_app.test_client()
        self.login_url = '/api/v1/auth/login'
        self.user = dict(email="testuser@gmail.com", password="testpass1234")
        self.unknown = dict(email="username@gmail.com", password="password")
        self.register = self.app.post('/api/v1/auth/register',
                                      data=json.dumps(self.user),
                                      headers={"content-type": "application/json"})
        self.login = self.app.post(self.login_url, data=json.dumps(self.user), content_type='application/json')
        self.data = json.loads(self.login.get_data(as_text=True))
        self.token = self.data['token']
        self.app.post("/api/v1/auth/register", data=json.dumps(self.unknown),content_type="application/json")
        self.missing_email = dict(email="", password="testpass")
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
        self.sale = dict(name="Shoes", description="All kinds of shoes", quantity=50, total="10000")
        self.new_sale = dict(name="Spoons", description="Ni vijiko jamani", quantity=120, total="3000")
        self.empty_sale = dict(name="", description="", quantity=0, total="")
        self.missing_sale_quantity = dict(name="Spoons", description="Ni vijiko jamani", quantity=0, total="3000")
        self.missing_sale_description = dict(name="Spoons", description="", quantity=120, total="3000")
        self.missing_sale_total = dict(name="Spoons", description="Ni vijiko jamani", quantity=120, total="")
        self.wrong_email_format = dict(email="1234.xxx", password="testpass")
        self.invalid_email = dict(emaile="testuser.gmail.com", password="invalid")
        self.invalid_password = dict(email="testuser3@gmail.com", password="t")
        self.password_spaced = dict(email="testuser5@gmail.com", password="  ")
        self.unknown_login = self.app.post("/api/v1/auth/login", data=json.dumps(self.unknown),
                                           content_type="application/json")
        self.data = json.loads(self.unknown_login.get_data(as_text=True))
        self.unknown_token = self.data['token']
