import json
import unittest
from app.tests.test_basecase import TestSetUp
from app.api.v1.models import Product


class TestProductModel(TestSetUp):
    """This class holds test cases for the products endpoints"""

    def test_product_creation(self):
        """Tests whether our API can create a product"""
        response = self.app.post('/api/v1/products',
                                 data=json.dumps(self.new_product),
                                 content_type="application/json",
                                 headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Product", response_msg["Message"])

    def test_product_access_with_invalid_token(self):
        """Raise unauthorized error when invalid token is used"""
        response = self.app.post("/api/v1/products",
                                 data=json.dumps(self.product),
                                 content_type="application/json",
                                 headers={"x-access-token": "Wrong token"})
        self.assertEqual(response.status_code, 401)

    def test_find_product_by_id(self):
        """Tests whether our API can find a product by its id"""
        self.app.post('/api/v1/products', data=json.dumps(self.product),
                      content_type="application/json",
                      headers={"x-access-token": self.token})
        resp = self.app.get('/api/v1/products/1')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_get_all_products(self):
        """Test whether API can list all items"""
        resp = self.app.get('/api/v1/products')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_missing_product_name(self):
        """Test that API should not accept missing product name"""
        response = self.app.post("/api/v1/products",
                                 data=json.dumps(dict(name="")),
                                 content_type="application/json",
                                 headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("required", response_msg["Message"])

    def test_missing_product_descr(self):
        """Test that API should not accept missing product description"""
        response = self.app.post("/api/v1/products",
                                 data=json.dumps(self.missing_prod_description),
                                 content_type="application/json",
                                 headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("required", response_msg["Message"])

    def test_missing_category(self):
        """Test that API should not accept missing product category"""
        response = self.app.post("/api/v1/products",
                                 data=json.dumps(self.missing_prod_category),
                                 content_type="application/json",
                                 headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("required", response_msg["Message"])

    def test_product_update(self):
        """Tests that the API can update a product"""
        response = self.app.put("/api/v1/products/1",
                                data=json.dumps(dict(name="Cup", description="Ni kikombe tu", price="100",
                                                     category="cutlery")),
                                content_type="application/json",
                                headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("updated", response_msg["Message"])

    def test_product_delete(self):
        """Tests that the API can delete a product."""
        self.app.post(
            '/api/v1/products',
            data=json.dumps(
                dict(
                    name="spoon",
                    description="metallic spoon",
                    price="20",
                    category="cutlery")),
            content_type="application/json",
            headers={
                "x-access-token": self.token}
        )
        response = self.app.delete("/api/v1/products/2",
                                   content_type="application/json",
                                   headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("deleted", response_msg["Message"])

    def test_invalid_delete_request(self):
        """Tests that the API raises an error when user places an invalid delete request"""
        response = self.app.delete("/api/v1/products/10",
                                   content_type="application/json",
                                   headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 404)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("not found", response_msg["Message"])

    def test_unauthorized_delete(self):
        """Tests that API prevents unauthorized user from deleting a product"""
        response = self.app.delete("/api/v1/products/2",
                                   content_type="application/json",
                                   headers={"x-access-token": "token_is_wrong"})
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Invalid", response_msg["Message"])

    def test_for_non_duplicates(self):
        """Tests that API can raise an error if you try to add a
        product that is in the list"""
        response = self.app.post("/api/v1/products",
                                 data=json.dumps(self.product),
                                 content_type="application/json",
                                 headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("already exists", response_msg["Message"])

    def tearDown(self):
        prod_obj = Product()
        prod_obj.products.clear()


if __name__ == "__main__":
    unittest.main()
