import json
import unittest
from app.tests.test_basecase import TestSetUp
from app.api.v1.models import Sales


class TestSalesModel(TestSetUp):
    """This class holds test cases for the sales endpoints"""

    def test_sale_creation(self):
        """Tests whether our API can create a sale record"""
        response = self.app.post('/api/v1/sales',
                                 data=json.dumps(self.new_sale),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Sale", response_msg["Message"])

    def test_find_sale_by_id(self):
        """Tests whether our API can find a sale record by sale id"""
        self.app.post('/api/v1/sales', data=json.dumps(self.sale),
                      content_type="application/json")
        resp = self.app.get('/api/v1/sales/1')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_get_all_sales(self):
        """Test whether API can list all sales in the sales list"""
        resp = self.app.get('/api/v1/sales')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_missing_sale_name(self):
        """Test that API should not accept missing sale name"""
        response = self.app.post("/api/v1/sales",
                                 data=json.dumps(dict(name="")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("required", response_msg["Message"])

    def test_missing_sale_descr(self):
        """Test that API should not accept missing sale description"""
        response = self.app.post("/api/v1/sales",
                                 data=json.dumps(self.missing_sale_description),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("required", response_msg["Message"])

    def test_missing_quantity(self):
        """Test that API should not accept missing sale quantity"""
        response = self.app.post("/api/v1/sales",
                                 data=json.dumps(self.missing_sale_quantity),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("required", response_msg["Message"])

    def test_missing_price(self):
        """Test that API should not accept missing sale total"""
        response = self.app.post("/api/v1/sales",
                                 data=json.dumps(self.missing_sale_total),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("required", response_msg["Message"])

    def test_sale_update(self):
        """Tests that the API can update a sale record"""
        response = self.app.put("/api/v1/sales/1",
                                data=json.dumps(dict(name="Cups", description="Ni vikombe jamani", quantity="120",
                                                     total="3000")),
                                content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("updated", response_msg["Message"])

    def test_sale_delete(self):
        """Tests that the API can delete a sale."""
        self.app.post(
            '/api/v1/products',
            data=json.dumps(
                dict(
                    name="Phones",
                    description="Android and iOS Phones",
                    quantity="20",
                    total="50000")),
            content_type="application/json"
        )
        response = self.app.delete("/api/v1/sales/2",
                                   content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("deleted", response_msg["Message"])

    def test_for_non_duplicates(self):
        """Tests that API can raise an error if you try to add a
        product that is in the list"""
        response = self.app.post("/api/v1/sales",
                                 data=json.dumps(self.sale),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("already exists", response_msg["Message"])

    def tearDown(self):
        """Creates a sales object and uses it to destroy the sales dictionary"""
        sales_obj = Sales()
        sales_obj.Sales.clear()

if __name__ == "__main__":
    unittest.main()
