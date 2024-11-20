document.getElementById('chat-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const userInput = document.getElementById('chat-input').value.toLowerCase();
    const chatLog = document.getElementById('chat-log');

    const userMessage = document.createElement('div');
    userMessage.textContent = `You: ${userInput}`;
    chatLog.appendChild(userMessage);

    try {
        const response = await fetch('http://127.0.0.1:5000/query', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ input: userInput })
        });

        if (response.ok) {
            const result = await response.json();
            const botMessage = document.createElement('div');
            botMessage.textContent = `Bot: ${result.response}`;
            chatLog.appendChild(botMessage);
        } else {
            const botMessage = document.createElement('div');
            botMessage.textContent = `Bot: Sorry, something went wrong.`;
            chatLog.appendChild(botMessage);
        }

    } catch (error) {
        const botMessage = document.createElement('div');
        botMessage.textContent = `Bot: Sorry, I could not reach the server.`;
        chatLog.appendChild(botMessage);
    }

    document.getElementById('chat-input').value = '';
    chatLog.scrollTop = chatLog.scrollHeight;
});
