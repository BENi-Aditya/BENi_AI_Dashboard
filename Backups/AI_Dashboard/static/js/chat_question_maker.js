$(document).ready(function() {
    $('#questionMakerForm').on('submit', function(e) {
        e.preventDefault();
        const userInput = $('#user-input').val();
        $('#chat-box').append('<div class="message user-message">' + userInput + '</div>');
        $('#user-input').val('');

        $.ajax({
            url: '/question_maker',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ user_input: userInput }),
            success: function(response) {
                $('#chat-box').append('<div class="message bot-message">' + response.response + '</div>');
            },
            error: function() {
                $('#chat-box').append('<div class="message bot-message">Failed to get response from Question Maker</div>');
            }
        });
    });
});