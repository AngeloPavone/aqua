from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__, static_folder="static")
app.config['SECRET_KEY'] = "dontworryaboutitbruh"
io = SocketIO(app)


@app.route("/", methods=["GET", "POST"])
def index() -> str:
    return render_template("index.html")


def message_confirm(message, methods=["GET","POST"]) -> None:
    print(f"message: {message}")


@io.on('send_message')
def handle_message(message) -> None:
    message_confirm(message)
    io.emit('receive_message', {'message': message}, broadcast=True)


def main() -> None:
    io.run(app, debug=True)

if __name__ == '__main__':
    main()
