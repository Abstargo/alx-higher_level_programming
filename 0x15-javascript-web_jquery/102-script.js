$(document).ready(function () {
	//Event handler for adding a new <li> item
	$('add_item').click(function() {
		$('ul.my_list').append('<li>Item</li>');
	});

	//Event handler for removing the last <li> item
	$('#removing_item').click(function() {
		$('ul.my_list li:last-child').remove();
	});

	//Event handler for clearing all <li> items
	$('#clear_list').click(function() {
		$('ul.my_list').empty();
	});
});
