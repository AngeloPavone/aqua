// Connect to socket.IO server
const socket = io('http://127.0.0.1:5000')

// Send the message to the server
// TODO: Implement input sanitization so you cannot send empty messages 
const messageInput = document.getElementById('message-input');
if (document.getElementById('message-input').value != null) {
	document.querySelector('form.chatbox').addEventListener('submit', function(e) {
		e.preventDefault();
		message = messageInput.value
		socket.emit('send_message', message);
		document.getElementById('message-input').value = null;
	});

	messageInput.addEventListener('keydown', function(e) {
		if (e.key === "Enter" && !e.shiftKey) {
			e.preventDefault();
			messageInput.form.dispatchEvent(new Event('submit'));
		}
	});
}

// Receive a message from the server
socket.on('receive_message', function(data) {
	const chatContainer = document.getElementById('chat-container');
	const messageContainer = document.createElement('div');
	messageContainer.classList.add('message-container');
	messageContainer.classList.add(data.position);
	
	const messageBubble = document.createElement('div');
	messageBubble.classList.add('message-bubble');
	messageBubble.innerHTML = data.message;
	
	messageContainer.appendChild(messageBubble);
	chatContainer.appendChild(messageContainer);
  });
