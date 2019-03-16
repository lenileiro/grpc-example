let grpc = require("grpc");
var grpc_promise = require('grpc-promise')
var client = require('./credentials')

async function fetch(name) {
    const meta = new grpc.Metadata();
    meta.add('key', 'value');

    grpc_promise.promisifyAll(client, { metadata: meta, timeout: 1000 }); // timeout in milliseconds
    
    var response = client.SayHello()
    .sendMessage({name: name})

    return response
}

response = fetch("sam")

response.then(data => {
    console.log('Client:', data)
})