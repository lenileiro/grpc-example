import logging
import time
from concurrent import futures

import grpc
import hello_pb2
import hello_pb2_grpc

class Greeter(hello_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        print('Send: Hello, %s!' % request.name)
        return hello_pb2.HelloReply(message='Hello, %s!' % request.name)

class Server:
    @staticmethod
    def get_credentials():
        # read in certificate
        try:
            with open('keys/ca.crt', 'rb') as f:
                trusted_certs = f.read()
            
            with open('keys/server.key', 'rb') as f:
                server_key = f.read()

            with open('keys/server.crt', 'rb') as f:
                server_cert = f.read()

        except Exception as e:
            log.error('failed-to-read-cert-keys', reason=e)

        # create credentials
        credentials = grpc.ssl_server_credentials([(server_key, server_cert)], trusted_certs)
        return credentials
    
    @staticmethod
    def serve():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
        
        server_credentials = Server.get_credentials()
        
        server.add_secure_port('localhost:50051', server_credentials)
        server.start()
        try:
            while True:
                time.sleep(10)
        except KeyboardInterrupt:
            server.stop(0)

    def end():
        raise KeyboardInterrupt


if __name__ == '__main__':
    print("server has started")
    logging.basicConfig()
    Server.serve()