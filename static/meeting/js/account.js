$(document).ready(function(){
	$('#change_password_form').submit(function(e){
		e.preventDefault();
		var current_password = $('#current_password').val();
		var new_password_1 = $('#new_password_1').val();
		var new_password_2 = $('#new_password_2').val();

		if (current_password == ''){
			alert("Current Password submitted empty.");
			return 0;
		}
		if (new_password_1 == '' || new_password_2 == ''){
			alert("New Password field submitted empty.");
			return 0;
		}


		var context = {
			'current_password': current_password,
			'new_password_1': new_password_1,
			'new_password_2': new_password_2
		};

		$.ajax({
			type: 'POST',
			url: '/change_password/',
			data: {			'current_password': current_password,
			'new_password_1': new_password_1,
			'new_password_2': new_password_2,
			'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
		},
			success: function(){
				location.reload();
			}
		});
		

	});
});