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

				//open the file
				fs.readFile(file, 'utf-8' ,function(errors, file_data){
					
					if(errors){throw errors;}
					// replace data file_data
					for(var key in items){
						// an ugly trick to imitate an `String.replaceAll()` method
						file_data = file_data.split('{{'+key+'}}').join(items[key]);
					}
					response.write(file_data);
					// close 
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
			var signal_name = controller+'#'+action;
			emiter.emit(signal_name, response, data );



			console.log(response.render)

			

		}).listen(port);

		return emiter;
	}
}



module.exports = App
