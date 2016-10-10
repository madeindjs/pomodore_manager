var http = require('http');


var server = http.createServer(function(req, res) {
  res.writeHead(200, {"Content-Type": "text/html"});
  res.end('Salut tout le monde !');
});

server.listen(12345);