$(document).ready(function() {
    $('#documentAnalysisForm').on('submit', function(e) {
        e.preventDefault();
        const formData = new FormData();
        const fileInput = document.getElementById('file-input');
        formData.append('file', fileInput.files[0]);

        $.ajax({
            url: '/document_analysis',
            type: 'POST',
            data: formData,
            contentType: false,
            processData: false,
            success: function(response) {
                $('#chat-box').append('<div class="message bot-message">' + response.response + '</div>');
            },
            error: function() {
                $('#chat-box').append('<div class="message bot-message">Failed to get response from Document Analysis</div>');
            }
        });
    });
});