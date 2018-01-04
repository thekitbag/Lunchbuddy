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

$(function(){
	$('#btnGetAllDestinations').click(function(){
		
		$.ajax({
			url: '/getAllDestinations',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				$('#destinationList tbody tr').remove();
				var results = response;
				var resultsLength = results.length;
				var table = document.getElementById('destinationList').getElementsByTagName('tbody')[0];
				for (var i = 0; i < resultsLength; i++) {
					var row = table.insertRow();
					var cell1 = row.insertCell();
					var cell2 = row.insertCell();
					cell1.innerHTML = results[i]
					cell2.innerHTML = "<button>EDIT</Button>"

				

				};
			},
			error: function(error){
				console.log(error);
			}
		});		
	});
});

