% include('_layout_header')

<h2>Tasks</h2>

<ul class="tasks">
	% for task in tasks:
		<li>
			<strong>{{task.name}}</strong> {{task.description}}
			<ul class="actions">
				<li><a href="/tasks/delete/{{task.id}}"><img src="/static/ic_delete.svg" alt="add"/></a></li>
			</ul>
		</li>
	% end
</ul>

<a id="add" href="/tasks/new"><img src="/static/ic_add.svg" alt="add"/></a>

% include('_layout_footer')