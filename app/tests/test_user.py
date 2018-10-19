import unittest
import json
from app.tests.test_basecase import TestSetUp
from app.api.v1.views.user_view import user_object


class UserLoginClass(TestSetUp):
    """This class holds methods that test for user routes functionality"""

    def test_user_can_register(self):
        """Test if API can add new user"""
        response = self.app.post(
            "/api/v1/auth/register",
            data=json.dumps(dict(email="testuser1@gmail.com", password="testpass11234")),
            content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("registered", response_msg["Message"])

    def test_blank_email(self):
        """Tests if error is raised when email is missing."""
        response = self.app.post("/api/v1/auth/register",
                                 data=json.dumps(self.missing_email),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("required", response_msg["Message"])

    def test_missing_password(self):
        """Tests if error is raised when password is missing."""
        response = self.app.post("/api/v1/auth/register",
                                 data=json.dumps(dict(email="testuser2@gmail.com", password="")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("required", response_msg["Message"])

    def test_wrong_email_format(self):
        """Tests error raised when wrong email format is provided."""
        response = self.app.post("/api/v1/auth/register",
                                 data=json.dumps(self.wrong_email_format),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Wrong", response_msg["Message"])

    def test_get_all_users(self):
        """Test if API can get all registered users of the app"""
        response = self.app.get('/api/v1/auth/users',
                                content_type="application/json",
                                headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 200)

    def test_valid_login_generates_auth_token(self):
        """Tests token is generated on successful login."""
        response = self.app.post("/api/v1/auth/login",
                                 data=json.dumps(self.user),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("token", response_msg)

    def test_user_can_reset_password(self):
        # tests if the API can change a user's password
        """Register a user"""
        self.app.post('/api/v1/auth/register', data=json.dumps(self.user),
                      headers={"content-type": "application/json"})

        # login the just registered user and get a token
        self.login = self.app.post(
            '/api/v1/auth/login',
            data=json.dumps(
                self.user),
            content_type='application/json')
        self.data = json.loads(self.login.get_data(as_text=True))
        self.token = self.data['token']
        # Then reset their password with the new token
        response = self.app.put(
            '/api/v1/auth/reset-password',
            data=json.dumps(
                dict(
                    password="new_pass")),
            content_type="application/json",
            headers={
                "x-access-token": self.token})
        self.assertEqual(response.status_code, 202)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("updated", response_msg["Message"])

    def test_valid_logout(self):
        """Tests for a valid user logout"""
        response = self.app.delete(
            '/api/v1/auth/logout',
            headers={
                "x-access-token": self.token})
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("out", response_msg["Message"])

    def test_repeat_logout(self):
        """Test that API should prevent a user from logging out twice"""
        self.app.delete(
            '/api/v1/auth/logout',
            headers={
                "x-access-token": self.token})
        response = self.app.delete(
            '/api/v1/auth/logout',
            headers={
                "x-access-token": self.token})
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Already", response_msg["Message"])

    def tearDown(self):
            """ clear data after every test"""
            user_object.users.clear()


if __name__ == '__main__':
    unittest.main()
