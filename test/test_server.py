import unittest
from .client import Client

class CommentsTestClass(unittest.TestCase):

    def test_response(self):
        self.assertEqual(Client.run("sam"), 'Hello, sam!')
