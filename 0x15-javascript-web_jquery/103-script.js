$(document).ready(function() {
    // Function to fetch and display translation of "Hello"
    function fetchTranslation() {
        // Get the language code entered by the user
        var languageCode = $('#language_code').val();

        // Make an AJAX GET request to fetch the translation
        $.ajax({
            url: 'https://www.fourtonfish.com/hellosalut/hello/',
            method: 'GET',
            dataType: 'json',
            data: {
                lang: languageCode
            },
            success: function(response) {
                // Display the translation of "Hello" in the DIV#hello
                $('#hello').text(response.hello);
            },
            error: function(xhr, status, error) {
                // Display an error message if the translation request fails
                $('#hello').text('Error fetching translation');
                console.error('Error fetching translation:', error);
            }
        });
    }

    // Trigger translation when the Translate button is clicked
    $('#btn_translate').click(fetchTranslation);

    // Trigger translation when Enter key is pressed
    $('#language_code').keypress(function(event) {
        if (event.which === 13) { // 13 is the Enter key code
            fetchTranslation();
        }
    });
});
