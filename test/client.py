import grpc
import hello_pb2
import hello_pb2_grpc
from credentials.client import Credentials

def run():
    credentials = Credentials.get_credentials()
    channel = grpc.secure_channel('localhost:50052', credentials)
    stub = hello_pb2_grpc.GreeterStub(channel)

    return stub

class Client:
    @staticmethod
    def sayhello(name):
        stub = run()
        response = stub.SayHello(hello_pb2.HelloRequest(name=name))
        return response.message