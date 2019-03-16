var implsayHello = require('./implimentation')

function response(_, response){
    console.log('Greeting:', response.message);
  };

function run() {
    implsayHello('james', response)
}

run()