import uuid
import re


class User(object):
    """Store user data in dictionaries"""

    def __init__(self):
        self.users = {}
        self.u_token = {}

    def create_user(self, username, password, admin=False):
        """Creates a new user and appends them to the list of users"""
        data = {'id': uuid.uuid4(),
                'email': username,
                'password': password,
                'admin': admin}
        self.users[username] = data
        return self.users

    @staticmethod
    def validate_email(email):
        """This method uses a regular expression to validate email entered by user"""
        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
            return True
        return False
