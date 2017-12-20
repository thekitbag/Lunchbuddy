$(function(){
	$('#btnGetLunches').click(function(){
		
		$.ajax({
			url: '/findLunch',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				var results = response;
				var resultsLength = results.length;
				var table = document.getElementById('resultsTable');
				for (var i = 0; i < resultsLength; i++) {					
					var row = table.insertRow();
					var cell1 = row.insertCell();
					cell1.innerHTML = results[i]				    
				    //Do something
				};
			},
			error: function(error){
				console.log(error);
			}
		});		
	});
});
