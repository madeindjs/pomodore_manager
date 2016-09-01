<!DOCTYPE html>
<html>
<head>
	<title>Tasks#Index</title>
	<link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
	<h1>Tasks</h1>

	<ul>
		% for task in tasks:
			<li><strong>{{task.name}}</strong> {{task.description}}</li>
		% end
	</ul>

	<a href="/tasks/new">Add a new task</a>
</body>
</html>