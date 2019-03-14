"""Generates protocol messages and gRPC stubs."""

from grpc_tools import protoc

protoc.main((
    '',
    '-I=./protos',
    '--python_out=.',
    '--grpc_python_out=.',
    './protos/hello.proto',
))

print('python proto functions generated')