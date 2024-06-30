document.getElementById('chat-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const userInput = document.getElementById('user-input').value;
    const response = await fetch('/question_maker', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `user_input=${encodeURIComponent(userInput)}`
    });
    const data = await response.json();
    document.getElementById('chat-response').innerText = data.response;
});