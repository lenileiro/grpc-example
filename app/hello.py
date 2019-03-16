import grpc
import hello_pb2
import hello_pb2_grpc
from utils.tokens import Token

class Greeter(hello_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        for key, value in context.invocation_metadata():
            print('Received initial metadata: %s:  %s' % (key, value))

        token = Token.generate_token(name=request.name)


        #context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        #context.set_details('Invalid username or password')
        #docs https://github.com/grpc/grpc/blob/master/doc/statuscodes.md
        return hello_pb2.HelloReply(
            message='Hello, %s!' % request.name,
            token=token)

    def payload(self, request, context):
        token = request.token
        print(token)
        #payload = Token.decode_token()
        #return hello_pb2.PayloadResponse(payload=payload)