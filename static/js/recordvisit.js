$(function(){
	$('#btnEnter').click(function(){
		
		$.ajax({
			url: '/enterDetails',
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