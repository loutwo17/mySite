$(document).ready(funtion(){

		$('form').on('submit', function(event) {


			$.ajax({
				data : {
					firstname : $('first_name').val();
				},
				type : 'post',
				url : '/process'
			})
			.done(function(data) {
				if (data) {

					$('#success_message').show();
				}


			});

			event.preventDefault();
		});
});

