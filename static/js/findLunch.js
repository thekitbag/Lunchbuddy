$(function(){
	$('#btnGetLunches').click(function(){
		
		$.ajax({
			url: '/findLunch',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				var results = response;
				var resultsLength = results.length;
				for (var i = 0; i < resultsLength; i++) {
				    window.alert(results[i]);
				    //Do something
				};
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