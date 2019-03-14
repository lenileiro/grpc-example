
class sayHello{

    constructor(_client){
  
      this.client = _client
      this.user = sayHello.getUser()
      this.callback = sayHello.callback
  
      let state = {
        client: this.client,
        user: this.user,
        callback: this.callback
      }

      sayHello.response(state)
    }
    
    static response(state) {
  
      state.client.sayHello(
        {name: state.user},
        state.callback
        );
    } 
    
    static getUser(){
      var user;
        if (process.argv.length >= 3) {
            user = process.argv[2];
        } else {
            user = 'world';
        }
      return user
    }

    static callback(err, response){
      if (err){
        print(`error occured ${err}`)
      }
      console.log('Greeting:', response.message);
    };
  }

module.exports = function implsayHello(client){
    return new sayHello(client);
}