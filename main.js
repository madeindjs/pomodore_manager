var server = require('./server').start(12345);

server.on('root', function(response){
	response.write('hello')
})