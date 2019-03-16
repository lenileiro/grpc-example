import grpc
import hello_pb2
import hello_pb2_grpc
from utils.tokens import Token
from utils.validation import ErrorHandler

class Greeter(hello_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):

        self.error_handers(request, context)
        self.auth_handers(request, context)
        

        token = Token.generate_token(name=request.name)

        #docs https://github.com/grpc/grpc/blob/master/doc/statuscodes.md
        return hello_pb2.HelloReply(
            message='Hello, %s!' % request.name,
            token=token)
    
    def error_handers(self, request, context):
        #handle all defined fields
        ErrorHandler.isvalid('name',request.name, context)
        ErrorHandler.isvalid('id',request.id, context)
    
    def auth_handers(self, request, context):
        for key, value in context.invocation_metadata():
            if key == 'token':
                payload = Token.decode_token(value)
                print('Received : %s' % (payload))
                break
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details('Token metadata is required')
