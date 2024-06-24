
async function sendMessage() {
    const userInput = document.getElementById('userInput').value;
    const chatContent = document.getElementById('chatContent');
    if (userInput) {
        const userMessage = document.createElement('div');
        userMessage.textContent = 'You: ' + userInput;
        chatContent.appendChild(userMessage);

        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userInput })
        });
        const data = await response.json();

        const aiResponse = document.createElement('div');
        aiResponse.textContent = 'AI: ' + data.chat_response;
        chatContent.appendChild(aiResponse);

        // Display NLU response if available
        if (data.nlu_response) {
            const nluResponse = document.createElement('div');
            nluResponse.textContent = 'NLU Response: ' + JSON.stringify(data.nlu_response);
            chatContent.appendChild(nluResponse);
        }

        // Display TTS response if available
        if (data.tts_response) {
            const audioPlayer = document.getElementById('audioPlayer');
            audioPlayer.src = 'data:audio/wav;base64,' + data.tts_response;
            audioPlayer.style.display = 'block';
            audioPlayer.play();
        }

        document.getElementById('userInput').value = '';
    }
}

    document.getElementById('imageUploadForm').addEventListener('submit', async (event) => {
        event.preventDefault();
        const formData = new FormData(event.target);
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        alert('Visual Search Result: ' + JSON.stringify(data));
    });
