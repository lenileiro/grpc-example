import unittest
from .client import Client


class CommentsTestClass(unittest.TestCase):

    def setUp(self):
        
        self.res= Client.run("sam")
    
    def test_response(self):
        self.assertEqual(self.res, 'Hello, sam!')
