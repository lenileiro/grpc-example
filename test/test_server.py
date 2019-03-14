import unittest
from server import Server
from .client import Client

server = Server()
class CommentsTestClass(unittest.TestCase):

    def setUp(self):
        #self.server=server
        #self.server.serve()
        self.res= Client.run("sam")

    def tearDown(self):
        self.res= Client.run("end")
        #server.serve(1)
        #Server.serve(0)

    def test_response(self):
        self.assertEqual(self.res, 'Hello, sam!')
