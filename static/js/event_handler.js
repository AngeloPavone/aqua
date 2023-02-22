// Connect to socket.IO server
const socket = io('http://127.0.0.1:5000')

let client_id = null

// Send the message to the server
const messageInput = document.getElementById('message-input');
document.querySelector('form.chatbox').addEventListener('submit', function(e) {
	e.preventDefault();
	const messageValue = {
		users: client_id,
		message: messageInput.value
	}
	if (messageValue['message'] != null && messageValue['message'].trim().length !== 0) {
		socket.emit('send_message', messageValue);
	}
	document.getElementById('message-input').value = null;
});

messageInput.addEventListener('keydown', function(e) {
	if (e.key === "Enter" && !e.shiftKey) {
		e.preventDefault();
		messageInput.form.dispatchEvent(new Event('submit'));
	}
});

socket.on('connected', function(userID) {
	client_id = userID
	socket.emit('user', client_id);
});

// Receive a message from the server
socket.on('receive_message', function(data) {
	const chatContainer = document.getElementById('chat-container');
	const messageBubble = document.createElement('div');
	data['user']['user_id'] = 'WBwEsQ-T97MtQ0LgAAAr'
	if(data['user']['user_id'] === client_id['user_id']) {
		data.position = 'right-aligned';
	} else {
		data.position = 'left-aligned';
	}
	messageBubble.classList.add(data.position)
	messageBubble.innerHTML = data['message'][data['message'].length - 1];

	chatContainer.insertBefore(messageBubble, chatContainer.firstChild);
  });
