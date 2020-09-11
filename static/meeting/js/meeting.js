$(document).ready(function(){
	$(document).on('submit','#add_agenda_item', function(e){
		e.preventDefault();
		$.ajax({
			type:'POST',
			url:'/create_new_agenda_item/',
			data:{
				'agenda_header': $("#agenda_header").val(),
				'agenda_background': $("#agenda_background").val()
			},
			success:function(){
				window.reload();
			}

		});
	});
});