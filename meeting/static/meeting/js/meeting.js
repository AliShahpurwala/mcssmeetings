$(document).ready(function(){
	$(document).on('submit','#add_agenda_item', function(e){
		if ($("#agenda_header").val() == ""){
			alert("Agenda Header cannot be empty.");
			return 0;
		}
		if($("#agenda_background").val() == ""){
			alert("Agenda Background cannot be empty.");
			return 0;
		}
		e.preventDefault();
		$.ajax({
			type:'POST',
			url:'/create_new_agenda_item/',
			data:{
				'agenda_header': $("#agenda_header").val(),
				'agenda_background': $("#agenda_background").val(),
				'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
			},
			success:function(){
				location.reload();
			}

		});
	});
});