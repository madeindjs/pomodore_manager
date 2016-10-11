var http = require('http');
var url = require("url");
const EventEmitter = require("events");


var App = {
	start: function(port){

		var emiter = new EventEmitter() ;

		http.createServer(function(request, response){
			response.writeHead(200, {"Content-Type": "text/html"});


			var url_array = request.url.split('/') ;

			var controller = url_array[1] ;
			var action = url_array.length >= 3 ? url_array[2] : 'index' ;
			var id = url_array.length >= 4 ? url_array[3] : undefined ;

			var data = { controller: controller, action: action, id: id };
			console.log(data);

			var signal_name = controller+'#'+action;

			emiter.emit(signal_name, response, data );

			response.end();
		}).listen(port);

		return emiter;
	}
}



module.exports = App
