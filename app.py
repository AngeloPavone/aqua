from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit


app = Flask(__name__, static_folder="static")
# TODO: regenerate secret key and move it out of codebase (can be generated using < python -c 'import secrets; print(secrets.token_hex())' >)
app.config['SECRET_KEY'] = '35b0327899affed2bef8b9d11b046beccbe9dcabcdd58bfa21f292ff2a4d34c7'
io = SocketIO(app)


user_id = None
username = None
user_messages = []
users = {'user': user_id, 'username': username, 'messages': user_messages}


@app.route("/", methods=["GET", "POST"])
def index() -> str:
    return render_template("index.html")


# recieve the user_id when someone connectes
@io.on('user_id')
def user_id_confirm(data, methods=["GET","POST"]) -> None:
    if data:
        # print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m') # -> color text example and codes https://i.stack.imgur.com/6otvY.png
        print('\x1b[1;32;40m' + 'CONNECTED: ' + '\x1b[0m' + data)


# recieve the message from the client
@io.on('send_message')
def handle_message(data) -> None:
    user_messages.append(data['message'])
    emit('receive_message', users, broadcast=True)
    print(users)


# assign a user_id when a 'connect' event is emited
@io.on('connect')
def user_connected(data) -> None:
    users['user'] = request.sid
    users['username'] = "tempUsername:" + users['user']
    emit('connected', users)


def main() -> None:
    # io.run(app, host='0.0.0.0', debug=True) # use this to host it on lan for testing
    io.run(app, debug=True)

if __name__ == '__main__':
    main()
