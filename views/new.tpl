% include('_layout_header')

<h2>New Task</h2>

<form method="POST">
	<label>name</label><input type="text" name="name"><br/>
	<label>description</label><input type="text" name="description"><br/>
	<label>status</label><input type="text" name="status"><br/>

	<input type="submit" value="add">
</form>

% include('_layout_footer')