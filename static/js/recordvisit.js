$(function(){
	$('#enter').click(function(){
		
		$.ajax({
			url: '/enterLunchDetails',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});