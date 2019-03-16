import hello_pb2
import hello_pb2_grpc

class Greeter(hello_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        print('Send: Hello, %s!' % request.name)
        return hello_pb2.HelloReply(message='Hello, %s!' % request.name)
