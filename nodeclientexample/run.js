var implsayHello = require('./implimentation')

function response(err, response){
    if (err){
      print(`error occured ${err}`)
    }
    console.log('Greeting:', response.message);
  };

function run() {
    implsayHello('james', response)
}

run()