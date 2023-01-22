from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = "dontworryaboutitbruh"
socketio = SocketIO(app)


@app.route("/", methods=["GET", "POST"])
def home() -> str:
    return render_template("index.html")

def message_confirm(methods=["GET","POST"]) -> None:
    print(f"Message recieved")

@socketio.on("message_event")
def handle_message_event(json, methods=["GET","POST"]) -> None:
    print(f"Event received: {str(json)}")
    socketio.emit("my response", json, callback=message_confirm)

def main() -> None:
    socketio.run(app, debug=True)


if __name__ == '__main__':
    main()
