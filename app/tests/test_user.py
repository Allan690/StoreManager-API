import unittest
import json
from app.tests.test_basecase import TestSetUp
from app.api.v1.views.user_view import user_object


class UserLoginClass(TestSetUp):
    """This class holds methods that test for user routes functionality"""

    def test_user_can_register(self):
        """Test if API can add new user"""
        response = self.app.post(
            "/api/v1/register",
            data=json.dumps(self.user),
            content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("registered", response_msg["Message"])

    def test_blank_email(self):
        """Tests if error is raised when email is missing."""
        response = self.app.post("/api/v1/register",
                                 data=json.dumps(self.missing_email),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("required", response_msg["Message"])

    def test_missing_password(self):
        """Tests error raised when password is missing."""
        response = self.app.post("/api/v1/register",
                                 data=json.dumps(self.missing_password),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("required", response_msg["Message"])

    def test_wrong_email_format(self):
        """Tests error raised when wrong email format is provided."""
        response = self.app.post("/api/v1/register",
                                 data=json.dumps(self.wrong_email_format),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Wrong", response_msg["Message"])

    def test_get_all_users(self):
        """Test if get method gets all registered users"""
        response = self.app.get('/api/v1/users',
                                content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        """ clear data after every test"""
        user_object.users.clear()


if __name__ == '__main__':
    unittest.main()
