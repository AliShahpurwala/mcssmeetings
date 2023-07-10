$(document).ready(function(){

	const meetingId = $("#meeting_id").text();
	updateCommentsForAllAgendaItems(meetingId);

	const chatSocket = new WebSocket(
            'ws://'
            + window.location.host
            + '/ws/meeting/'
            + meetingId
            + '/'
        );

    chatSocket.onmessage = function(e) {
        updateCommentsForAllAgendaItems(meetingId);
    };

    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };

	function updateCommentsForAllAgendaItems(meetingId) {
		var agendaItemsForMeetings;
		fetch(`/meeting/${meetingId}/agendaItems`).then(
				(response) => { return response.json() }
			).then(
				(response) => { 
					agendaItemsForMeetings = JSON.parse(response); 
					for (i = 0; i < agendaItemsForMeetings.length; i++) {
						var agendaItemElem = $(`#comments_for_agenda_item_${agendaItemsForMeetings[i]["pk"]}`);
						fetch(`/agendaItem/${agendaItemsForMeetings[i]["pk"]}/comments`)
						.then((response) => { return response.json() })
						.then((response) => {
							var commentsForAgendaItem = JSON.parse(response);
							agendaItemElem.empty();
							for (x = 0; x < commentsForAgendaItem.length; x++) {

								agendaItemElem.append($("<p></p>").text(`${commentsForAgendaItem[x]["fields"]["author"]} : ${commentsForAgendaItem[x]["fields"]["text"]}`))
							}
						})
					}
				}
			).catch((error) => { console.error(error); });
	}

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

	$('form[name^="new_comment_"]').on('submit', function(e){
		e.preventDefault();
		var form_name = $(this).attr('name');
		var agenda_id = form_name.slice(12);
		var comment_text = $("#comment_for_item_" + agenda_id + "_text").val();
		$("#comment_for_item_" + agenda_id + "_text").val("");
		$.ajax({
			type: 'POST',
			url: '/create_new_comment_item/',
			data: {
				'agenda_id': agenda_id,
				'comment_text': comment_text,
				'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()	
			},
			success:function(){
				chatSocket.send(JSON.stringify({"type": "reload"}));
				// location.reload();
			}
		});

		
	});
});