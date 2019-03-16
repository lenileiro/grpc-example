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
        #response = stub.SayHello(hello_pb2.HelloRequest(name=name, id=5))
        response, call = stub.SayHello.with_call(
        hello_pb2.HelloRequest(name=name, id=5),
        metadata=(
            ('token', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE1NTI3NjkyMzEsImlhdCI6MTU1Mjc2NzQzMSwibmFtZSI6InNhbSJ9.pflBwO7kA9ML7dKKQUMTUUnyHgRMovRvQcLbnQ1h2hPE6dlz9uPOoglGb12gyBf5kLxxng39HfU58kcHcxqDsrZ0CApQ28T018nENvEjBqR-WNxnWXvazzQxiFGPk5NAgGEpYnHwS8Bp0tEVW_1VLVTgrRgH8wL7m3DEsm51uJ9FNrfSNJKke3u5znNdhLNi7MuzLaFAe_rs5BnWLfAWP3TBaNTSzC9LKO8YAF0R-GXfC2Jz1ADCnx_LdAaoA8NtTpMInFxJqBJkjarMju0WHgwkt4qpfmjR3ku2mkEe7CnFLZSAOGWaYco_TFjX8Clm6IdmDiCQLPhm6MZcrXOOWw'),
        ))
        return response.message