import unittest
from server import Server
from .client import Client


class CommentsTestClass(unittest.TestCase):

    def setUp(self):
        self.res= Client.run("sam")

    def tearDown(self):
        pass
        #Server.serve(0)

    def test_response(self):
        self.assertEqual(self.res, 'Hello, sam!')
