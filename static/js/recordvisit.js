$(function(){
	$('#btnEnterDetails').click(function(){
		
		$.ajax({
			url: '/recordVisit',
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