% include('_layout_header')

<div id="delete"> </div>


<!-- <a id="add" href="/new"><img src="/static/ic_add.svg" alt="add"/></a> -->

<div id="new" ></div>

% for task in tasks:
	<div class="task" id="{{task.id}}">
		<strong>{{task.name}}</strong> {{task.description}}
	</div>
% end



% include('_layout_footer')