% include('_layout_header')

<a id="add" href="/new"><img src="/static/ic_add.svg" alt="add"/></a>

% for task in tasks:
	<div class="task">
		<strong>{{task.name}}</strong> {{task.description}}
		<ul class="actions">
			<li><a href="/update/{{task.id}}"><img src="/static/ic_edit.svg" alt="update"/></a></li>
			<li><a href="/delete/{{task.id}}"><img src="/static/ic_delete.svg" alt="add"/></a></li>
		</ul>
	</div>
% end


% include('_layout_footer')