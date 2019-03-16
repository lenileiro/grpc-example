import hello_pb2
import hello_pb2_grpc
from utils.tokens import Token

class Greeter(hello_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        token = Token.generate_token(name=request.name)
        return hello_pb2.HelloReply(
            message='Hello, %s!' % request.name,
            token=token)

    def payload(self, request, context):
        token = request.token
        print(token)
        #payload = Token.decode_token()
        #return hello_pb2.PayloadResponse(payload=payload)