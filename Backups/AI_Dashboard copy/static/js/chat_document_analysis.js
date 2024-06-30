document.getElementById('chat-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const fileInput = document.getElementById('file-input').files[0];
    const formData = new FormData();
    formData.append('file', fileInput);
    const response = await fetch('/document_analysis', {
        method: 'POST',
        body: formData
    });
    const data = await response.json();
    document.getElementById('chat-response').innerText = data.response;
});