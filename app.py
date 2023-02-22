from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit


app = Flask(__name__, static_folder="static")
# TODO: regenerate secret key and move it out of codebase (can be generated using < python -c 'import secrets; print(secrets.token_hex())' >)
app.config['SECRET_KEY'] = '35b0327899affed2bef8b9d11b046beccbe9dcabcdd58bfa21f292ff2a4d34c7'
io = SocketIO(app)


user_messages = []


@app.route("/", methods=["GET", "POST"])
def index() -> str:
    return render_template("index.html")


# recieve the user_id when someone connectes
@io.on('user_id')
def user_id_confirm(user_id, methods=["GET","POST"]) -> None:
    if user_id:
        print(user_id)


# recieve the message from the client
@io.on('send_message')
def handle_message(data) -> None:
    user_messages.append(data['message'])
    user_id = data['users']
    users = {'user': user_id, 'message': user_messages}
    emit('receive_message', users, broadcast=True)
    print(users)


# asign a user_id when socketio emits a 'connect' event
@io.on('connect')
def user_connected(user_id) -> None:
    user_id = request.sid #pyright: ignore
    emit('connected', {'user_id': user_id})


def main() -> None:
    # io.run(app, host='0.0.0.0', debug=True) # use this to host it on lan for testing
    io.run(app, debug=True)

if __name__ == '__main__':
    main()
