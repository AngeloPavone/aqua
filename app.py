from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__, static_folder="static")
app.config['SECRET_KEY'] = "dontworryaboutitbruh"
io = SocketIO(app)


@app.route("/", methods=["GET", "POST"])
def index() -> str:
    return render_template("index.html")


@io.on('user_id')
def user_id_confirm(user_id, methods=["GET","POST"]) -> None:
    print(user_id)


@io.on('send_message')
def handle_message(message) -> None:
    io.emit('receive_message', {'message': message})
    print(message)


@io.on('connect')
def test_connection(user_id) -> None:
    io.emit('connected', {'user_id': user_id})
    user_id_confirm(user_id)


def main() -> None:
    io.run(app, debug=True)

if __name__ == '__main__':
    main()
