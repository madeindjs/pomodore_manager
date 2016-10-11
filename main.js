var server = require('./server').start(12345);

server.on('tasks#index', function(response){
	response.write('<h1>task of index</h1>');
})

server.on('tasks#show', function(response, data){
	response.write('<h1>task n°'+data.id+'</h1>');
})