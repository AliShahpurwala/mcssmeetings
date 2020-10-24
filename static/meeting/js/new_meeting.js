$(document).ready(function(){
	$("#create_new_meeting_submit_button").click(function(){
		var meeting_header = $("#meeting_header").val();
		var start_time_string = $("#start_time").val();
		var end_time_string = $("#end_time").val();

		if (meeting_header == ""){
			alert("Meeting Header must be filled.");
			return 0;
		} 
		if (start_time_string == ""){
			alert("Start Time must be filled.");
			return 0;
		}
		if (end_time_string == ""){
			alert("End Time must be filled.");
			return 0;
		}
		var start_time = new Date(parseInt(start_time_string[0] + start_time_string[1] + start_time_string[2] + start_time_string[3]),
			parseInt(start_time_string[5] + start_time_string[6]) - 1,
			parseInt(start_time_string[8] + start_time_string[9]),
			parseInt(start_time_string[11] + start_time_string[12]),
			parseInt(start_time_string[14] + start_time_string[15])
			);
		var end_time = new Date(parseInt(end_time_string[0] + end_time_string[1] + end_time_string[2] + end_time_string[3]),
			parseInt(end_time_string[5] + end_time_string[6]) - 1,
			parseInt(end_time_string[8] + end_time_string[9]),
			parseInt(end_time_string[11] + end_time_string[12]),
			parseInt(end_time_string[14] + end_time_string[15])
			);
		if (start_time > end_time){
			alert("Start time can not be after the End time.");
		}
		document.create_new_meeting_form.submit()

	});

	
});