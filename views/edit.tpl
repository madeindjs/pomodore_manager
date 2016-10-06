% include('_layout_header')

<!-- It's the same form for a new / update task. if a task was send in context,
Python will include Python values in form-->

% if task :
	<h2>Update Task</h2>
% else:
	<h2>New Task</h2>
% end 


<form method="POST">
	<label>name</label><input type="text" name="name" 
		% if task != None :
			value="{{task.name}}"
		% end 
		><br/>
	<label>description</label><input type="text" name="description"
		% if task != None :
			value="{{task.description}}"
		% end 
		><br/>
	<label>status</label><input type="text" name="status"
		% if task != None :
			value="{{task.status}}"
		% end 
		><br/>

	<input type="submit" value="add">
</form>

% include('_layout_footer')