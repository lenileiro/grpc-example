let grpc = require("grpc");
var protoLoader = require("@grpc/proto-loader");
var implsayHello = require('./implimentation')
var fs = require('fs');

//Load the protobuf
var proto = grpc.loadPackageDefinition(
    protoLoader.loadSync("proto/hello.proto", {
      keepCase: true,
      longs: String,
      enums: String,
      defaults: true,
      oneofs: true
    })
  );

function main() {

    const cacert = fs.readFileSync('keys/ca.crt');
    const cert = fs.readFileSync('keys/client.crt');
    const key = fs.readFileSync('keys/client.key');

    let credentials = grpc.credentials.createSsl(cacert,key, cert);
    let client = new proto.helloworld.Greeter('localhost:50051', credentials);

    implsayHello(client)
}



main();