var http = require('http');
var url = require("url");
var fs = require("fs");
const EventEmitter = require("events");


var App = {
	start: function(port){

		var emiter = new EventEmitter() ;

		http.createServer(function(request, response){

			// create the function to render an Html file
			response.render = function(file, items){

				response.writeHead(200, {"Content-Type": "text/html"});

				//open the file
				fs.readFile(file, 'utf-8' ,function(errors, file_data){
					if(errors){throw errors;}
					
					// replace data file_data
					for(var key in items){// an ugly trick to imitate an `String.replaceAll()` method
						file_data = file_data.split('{{'+key+'}}').join(items[key]);
					}
					response.write(file_data);
					response.end();
				})// close file

			}

			// parse url
			var url_array = request.url.split('/') ;
			var controller = url_array[1] ;
			var action = url_array.length >= 3 ? url_array[2] : 'index' ;
			var id = url_array.length >= 4 ? url_array[3] : undefined ;
			var data = { controller: controller, action: action, id: id };
			console.log(data);

			//emit the signal
			var event_name = controller+'#'+action;
			// if no one listen this event, we raise a 404 error
			if(!emiter.emit(event_name, response, data )){
				response.writeHead(400);
				response.end();
			}		

		}).listen(port);

		return emiter;
	}
}



module.exports = App
