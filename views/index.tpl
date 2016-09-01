<!DOCTYPE html>
<html>
<head>
	<title>Tasks#Index</title>
	<link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
	<h1>Tasks</h1>

	<ul class="tasks">
		% for task in tasks:
			<li>
				<strong>{{task.name}}</strong> {{task.description}}
				<ul class="actions">
					<li><a href="/tasks/delete/{{task.id}}">delete</a></li>
				</ul>
			</li>
		% end
	</ul>

	<a href="/tasks/new">Add a new task</a>
</body>
</html>