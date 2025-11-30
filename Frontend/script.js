const chatContainer = document.getElementById('chat-container');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const welcomeMessage = document.querySelector('.welcome-message');

// Auto-resize textarea
userInput.addEventListener('input', function () {
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight) + 'px';
    if (this.value === '') {
        this.style.height = 'auto';
    }
});

// Handle Enter key
userInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

sendBtn.addEventListener('click', sendMessage);

async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    // Hide welcome message if it exists
    if (welcomeMessage) {
        welcomeMessage.style.display = 'none';
    }

    // Add user message
    addMessage(message, 'user');
    userInput.value = '';
    userInput.style.height = 'auto';

    // Show loading state
    const loadingId = addLoadingIndicator();

    try {
        const response = await fetch('http://localhost:8000/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });

        const data = await response.json();

        // Remove loading indicator
        removeMessage(loadingId);

        // Add bot response
        // Handle markdown-like bullet points from the agent
        const formattedResponse = formatResponse(data.response);
        addMessage(formattedResponse, 'bot', true);

    } catch (error) {
        console.error('Error:', error);
        removeMessage(loadingId);
        addMessage('Sorry, something went wrong. Please try again.', 'bot');
    }
}

function addMessage(text, sender, isHtml = false) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);

    const contentDiv = document.createElement('div');
    contentDiv.classList.add('message-content');

    if (isHtml) {
        contentDiv.innerHTML = text;
    } else {
        contentDiv.textContent = text;
    }

    messageDiv.appendChild(contentDiv);
    chatContainer.appendChild(messageDiv);

    // Scroll to bottom
    chatContainer.scrollTop = chatContainer.scrollHeight;

    return messageDiv.id = 'msg-' + Date.now();
}

function addLoadingIndicator() {
    const id = 'loading-' + Date.now();
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', 'bot');
    messageDiv.id = id;

    const contentDiv = document.createElement('div');
    contentDiv.classList.add('message-content');

    const indicator = document.createElement('div');
    indicator.classList.add('typing-indicator');

    for (let i = 0; i < 3; i++) {
        const dot = document.createElement('div');
        dot.classList.add('typing-dot');
        indicator.appendChild(dot);
    }

    contentDiv.appendChild(indicator);
    messageDiv.appendChild(contentDiv);
    chatContainer.appendChild(messageDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight;

    return id;
}

function removeMessage(id) {
    const element = document.getElementById(id);
    if (element) {
        element.remove();
    }
}

function formatResponse(text) {
    // Simple formatter for bullet points and newlines
    // Convert newlines to <br>
    let formatted = text.replace(/\n/g, '<br>');

    // Convert * bullet points to list items if they exist
    if (formatted.includes('* ')) {
        formatted = formatted.replace(/\* (.*?)(<br>|$)/g, '<li>$1</li>');
        // Wrap lists in <ul> if we found list items
        if (formatted.includes('<li>')) {
            formatted = '<ul>' + formatted + '</ul>';
        }
    }

    return formatted;
}
