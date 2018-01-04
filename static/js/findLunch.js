$(function(){
	$('#btnGetLunches').click(function(){
		
		$.ajax({
			url: '/findLunch',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				$('#resultsTable tbody tr').remove();
				var results = response;
				var resultsLength = results.length;
				var table = document.getElementById('resultsTable').getElementsByTagName('tbody')[0];
				for (var i = 0; i < resultsLength; i++) {
					var row = table.insertRow();					
					for (var j = 1; j < 8; j++){					
					var cell1 = row.insertCell();
					cell1.innerHTML = results[i][j]
				};

				};
			},
			error: function(error){
				console.log(error);
			}
		});		
	});
});

$(function(){
	$('#btnGetTakeAway').click(function(){
		
		$.ajax({
			url: '/findTakeAway',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				$('#resultsTable tbody tr').remove();
				var results = response;
				var resultsLength = results.length;
				var table = document.getElementById('resultsTable').getElementsByTagName('tbody')[0];
				for (var i = 0; i < resultsLength; i++) {
					var row = table.insertRow();					
					for (var j = 1; j < 8; j++){					
					var cell1 = row.insertCell();
					cell1.innerHTML = results[i][j]
				};

				};
			},
			error: function(error){
				console.log(error);
			}
		});		
	});
});

$(function(){
	$('#btnGetEatIn').click(function(){
		
		$.ajax({
			url: '/findEatIn',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				$('#resultsTable tbody tr').remove();
				var results = response;
				var resultsLength = results.length;
				var table = document.getElementById('resultsTable').getElementsByTagName('tbody')[0];
				for (var i = 0; i < resultsLength; i++) {
					var row = table.insertRow();					
					for (var j = 1; j < 8; j++){					
					var cell1 = row.insertCell();
					cell1.innerHTML = results[i][j]
				};

				};
			},
			error: function(error){
				console.log(error);
			}
		});		
	});
});

$(function(){
	$('#killserver').click(function(){
		
		$.ajax({
			url: '/shutdown',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response)
			},
			error: function(error){
				console.log(error);
			}
		});		
	});
});