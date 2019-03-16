var client = require('./connection')

module.exports = function implsayHello(user, func){

     // request method
     client.sayHello(
      {name: user},
      func
      );
}