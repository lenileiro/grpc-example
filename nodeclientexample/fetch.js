let grpc = require("grpc");
var grpc_promise = require('grpc-promise')
var client = require('./credentials')

function run() {
    const meta = new grpc.Metadata();
    meta.add('key', 'value');

    grpc_promise.promisifyAll(client, { metadata: meta, timeout: 1000 }); // timeout in milliseconds

    client.SayHello()
    .sendMessage({name: "sam"})
    .then(res => {
        console.log('Client:', res.message) // Client:Message Received
    })
    .catch(err => console.error(err))
}

run()