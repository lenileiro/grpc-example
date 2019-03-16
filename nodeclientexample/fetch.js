let grpc = require("grpc");
var grpc_promise = require('grpc-promise')
var client = require('./credentials')

function fetch(name) {
    const meta = new grpc.Metadata();
    meta.add('key', 'value');

    grpc_promise.promisifyAll(client, { metadata: meta, timeout: 1000 }); // timeout in milliseconds
    
    return client.SayHello()
    .sendMessage({name: name})
}


fetch("sam").then(res => {
    console.log('Client:', res.message) // Client:Message Received
})
.catch(err => console.error(err))