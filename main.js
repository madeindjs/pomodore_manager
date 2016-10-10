var http = require('http');
var url = require("url");

var port = 12345;

var server = http.createServer();
console.log('server started on localhost: http://localhost:'+port+'/')

server.on('request', function(req, res) {
  console.log( url.parse(req.url).pathname );
  res.writeHead(200, {"Content-Type": "text/html"});
  res.end('Salut tout le monde !');
})

server.on( 'close', function() {
  console.log('Bye bye !'); 
})

server.listen(port);