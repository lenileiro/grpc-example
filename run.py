import logging
import time
from concurrent import futures

import grpc
import hello_pb2
import hello_pb2_grpc
from credentials.server import Credentials
from app.hello import Greeter

def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    #register service to server
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    
    server_credentials = Credentials.get_credentials()
    
    server.add_secure_port('localhost:50051', server_credentials)
    server.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    print("server has started")
    logging.basicConfig()
    run()