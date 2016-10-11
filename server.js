var http = require('http');
var url = require("url");
const EventEmitter = require("events");


var App = {
	start: function(port){

		var emiter = new EventEmitter() ;

		http.createServer(function(request, response){
			response.writeHead(200, {"Content-Type": "text/html"});

			if(request.url === '/'){
				emiter.emit('root', response)
			}

			response.end();
		}).listen(port);

		return emiter;
	}
}



module.exports = App
