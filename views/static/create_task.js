$(document).ready(function(){

	$('#new').click(function(){

		var data = {name : "new task",
					description : "sweeet",
					status : "0"};

		$.ajax({

			url : '/new',
			type : 'POST',
			datatype: 'json',
			data : data ,
			success : function(response, statut){
				// delete the html tag
				var json = JSON.parse(response);
				console.log(json)
				var $div = $("<div>", {id: json['id'], "class": "task"});
				$div.html('<strong>'+json['name']+'</strong> '+json['description'] );
				$("body").append($div);
			},
			error : function(result, status, error){
				console.log('something goes wrong.. ' + error);
			}
	
		});

	});

})