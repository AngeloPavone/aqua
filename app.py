from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask("aqua")
app.config['SECRET_KEY'] = "dontworryaboutitbruh"
socketio = SocketIO(app)


@app.route("/", methods=["GET", "POST"])
def home() -> str:
    return render_template("index.html")

@socketio.on("message")
def handle_message(data) -> None:
    print(f"Message received: {data}")

def main() -> None:
    socketio.run(app, debug=True)


if __name__ == '__main__':
    main()
