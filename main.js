var server = require('./server').start(12345);

server.on('tasks#index', function(response){
	response.render('views/layout.html', {title: 'task of index'});
})

server.on('tasks#show', function(response, data){
	response.render('views/layout.html', {title: 'Task #'+data.id});
})