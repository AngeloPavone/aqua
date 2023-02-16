// Connect to socket.IO server
const socket = io('http://127.0.0.1:5000')

// Send the message to the server
const messageInput = document.getElementById('message-input');
document.querySelector('form.chatbox').addEventListener('submit', function(e) {
	e.preventDefault();
	message = messageInput.value
	if (message != null && message.trim().length !== 0) {
		socket.emit('send_message', message);
	}
	document.getElementById('message-input').value = null;
});

messageInput.addEventListener('keydown', function(e) {
	if (e.key === "Enter" && !e.shiftKey) {
		e.preventDefault();
		messageInput.form.dispatchEvent(new Event('submit'));
	}
});

// Receive a message from the server
socket.on('receive_message', function(data) {
	const chatContainer = document.getElementById('chat-container');
	const messageBubble = document.createElement('div');
	data.position = data.postion || "message-bubble"
	messageBubble.classList.add(data.position)

	messageBubble.innerHTML = data.message;

	chatContainer.insertBefore(messageBubble, chatContainer.firstChild);
  });
