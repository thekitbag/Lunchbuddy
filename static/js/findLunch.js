$(function(){
	$('#btnGetLunches').click(function(){
		
		$.ajax({
			url: '/findLunch',
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
$(function(){
	$("p").click(function(){
		$(this).hide();
    });
});