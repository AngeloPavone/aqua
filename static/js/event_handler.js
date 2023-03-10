// Connect to socket.IO server
const socket = io()

let client_id = null
let username = null

// Send the message to the server
const messageInput = document.getElementById('message-input');
document.querySelector('form.chatbox').addEventListener('submit', function(e) {
	e.preventDefault();
	const messageValue = {
		user: client_id,
		username: username,
		message: messageInput.value
	}
	if (messageValue['message'] !== null && messageValue['message'].trim().length !== 0) {
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

socket.on('connected', function(data) {
	client_id = data.user
	socket.emit('user_id', client_id);
});

// Receive a message from the server
socket.on('receive_message', function(data) {
	const chatContainer = document.getElementById('chat-container');
	const messageBubble = document.createElement('div');
	const username = document.getElementById('username');
	const otherUserName = document.getElementById('other-username')

	if(data['user'] === client_id) {
		data.position = 'right-aligned';
	} else {
		data.position = 'left-aligned';
	}

	let lastMessage = data.messages[data.messages.length - 1];
	messageBubble.classList.add(data.position);
	messageBubble.innerHTML = lastMessage;
	username.innerHTML = String(client_id);

	chatContainer.insertBefore(messageBubble, chatContainer.firstChild);

	for(const i in data) {
		console.log(i, data[i])
	}

  });
