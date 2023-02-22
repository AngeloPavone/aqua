from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit


app = Flask(__name__, static_folder="static")
# TODO: regenerate secret key and move it out of codebase (can be generated using < python -c 'import secrets; print(secrets.token_hex())' >)
app.config['SECRET_KEY'] = '35b0327899affed2bef8b9d11b046beccbe9dcabcdd58bfa21f292ff2a4d34c7'
io = SocketIO(app)


@app.route("/", methods=["GET", "POST"])
def index() -> str:
    return render_template("index.html")


@io.on('user_id')
def user_id_confirm(user_id, methods=["GET","POST"]) -> None:
    if user_id:
        print(user_id)


@io.on('send_message')
def handle_message(message) -> None:
    emit('receive_message', {'message': message}, broadcast=True)
    print(message)


@io.on('connect')
def user_connected(user_id) -> None:
    emit('connected', {'user_id': request.sid})
    print(user_id)


def main() -> None:
    io.run(app, debug=True)

if __name__ == '__main__':
    main()
