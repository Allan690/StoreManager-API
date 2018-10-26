import json
import unittest
from app.tests.test_basecase import TestSetUp
from app.api.v1.models.sale_models import Sales


class TestSalesModel(TestSetUp):
    """This class holds test cases for the sales endpoints and inherits from the TestSetUp class"""

    def test_sale_creation(self):
        """Tests whether our API can create a sale record"""
        self.app.post('/api/v1/products',
                      data=json.dumps(dict(name="Good shoes", description="Good shoes", price=1200,
                                quantity=30)),
                      content_type="application/json",
                      headers={"x-access-token": self.token})
        response = self.app.post('/api/v1/sales',
                                 data=json.dumps(dict(prod_id=1, quantity=5)),
                                 content_type="application/json",
                                 headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("updated", response_msg["Message"])

    def test_sale_access_with_invalid_token(self):
        """Raise unauthorized error when invalid token is used to access a sale"""
        self.app.post('/api/v1/products',
                      data=json.dumps(self.new_product),
                      content_type="application/json",
                      headers={"x-access-token": self.token})
        response = self.app.post("/api/v1/sales",
                                 data=json.dumps(self.sale),
                                 content_type="application/json",
                                 headers={"x-access-token": "Wrong token"})
        self.assertEqual(response.status_code, 401)

    def test_find_sale_by_id(self):
        """Tests whether our API can find a sale record by sale id"""
        self.app.post('/api/v1/products',
                      data=json.dumps(self.new_product),
                      content_type="application/json",
                      headers={"x-access-token": self.token})
        self.app.post('/api/v1/sales',
                      data=json.dumps(self.new_sale),
                      content_type="application/json",
                      headers={"x-access-token": self.token})
        resp = self.app.get('/api/v1/sales/1')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_get_all_sales(self):
        """Test whether API can list all sales in the sales list"""
        resp = self.app.get('/api/v1/sales')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_sale_quantity_is_zero(self):
        """Test that API should not accept zero sale quantity"""
        self.app.post('/api/v1/products',
                      data=json.dumps(self.new_product),
                      content_type="application/json",
                      headers={"x-access-token": self.token})
        response = self.app.post("/api/v1/sales",
                                 data=json.dumps(self.zero_sale_quantity),
                                 content_type="application/json",
                                 headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("required", response_msg["Message"])

    def test_sale_delete(self):
        """Tests that the API can delete a sale."""
        self.app.post('/api/v1/products',
                      data=json.dumps(self.product),
                      content_type="application/json",
                      headers={"x-access-token": self.token})
        self.app.post('/api/v1/sales',
                      data=json.dumps(self.new_sale),
                      content_type="application/json", headers={"x-access-token": self.token})
        response = self.app.delete("/api/v1/sales/2",
                                   content_type="application/json",
                                   headers={
                                       "x-access-token": self.token}
                                   )
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("deleted", response_msg["Message"])

    def test_invalid_delete_request(self):
        """Tests that the API raises an error when user places an invalid delete request"""
        response = self.app.delete("/api/v1/sales/10",
                                   content_type="application/json",
                                   headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 404)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("not found", response_msg["Message"])

    def tearDown(self):
        """Creates a sales object and uses it to destroy the sales dictionary"""
        sales_obj = Sales()
        sales_obj.Sales.clear()


if __name__ == "__main__":
    unittest.main()
