$(document).ready(function() {
	//Event handler for adding a new <li> item
	$('#add_item').click(function() {
		$('ul.my_list').append('<li>Itemw</li>');

	});

	//Event handler for removing the last <li> item
	$('#remove_item').click(function () {
		$('ul.my_list li:last-child').remove();
	});

	//Event handler for clearing all <li> items
	$('#clear_list').click(function () {
		$('ul.my_list').empty();
	});
});
