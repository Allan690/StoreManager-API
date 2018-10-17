import json
import unittest
import os
from src import app


class TestSetUp(unittest.TestCase):
    """Initialize the app with test data"""

    def setUp(self):
        self.app = app.test_client()
        self.user = {"email": "testuser@gmail.com", "password": "testpass"}
        self.unknownuser = {"email": "username@gmail.com", "password": "password"}
        self.product = {"name": "Shoe Polish",
                         "description": "Kiwi Shoe Polish",
                         "Price": "50",
                         "category": "accessories"#
                        }
        self.empty_product = {
                         "name": "Shoe Polish",
                         "description": "Kiwi Shoe Polish",
                         "Price": "50",
                         "category": "accessories"
                             }
        self.new_product = {
                            "name": "",
                            "description": "",
                             "Price": "",
                             "category": ""
                            }
