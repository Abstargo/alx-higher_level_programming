$(document).ready(function() {
	$('#btn_translate').click(function() {
		// Get the langauge code entered by the user
		var languageCode = $('#language_code').val();

		//Make an AJAX GET request to fetch the translationj
		$.ajax({
			url: 'https://www.fourtonfish.com/hellosalut/hello/',
			method: 'GET',
			dataType: 'json',
			data: {
				lang: languageCode
			},
			success: function(response) {
				//Display the translation of "Hello" in the DIV#hello
				$('#hello').text(response.hello);
			},
			error: function(xhr, status, error)
			{
				//Display an error message if the translation request fails
				$('#hello').text('Error fetching translation');
				console.error('Error fetching translation:', error);
			}
		});
	});
});
