from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__, static_folder="static")
app.config['SECRET_KEY'] = "dontworryaboutitbruh"
socketio = SocketIO(app)


chat_history = []


@app.route("/", methods=["GET", "POST"])
def home() -> str:
    return render_template("index.html")

def message_confirm(methods=["GET","POST"]) -> None:
    print(f"Message recieved")

@socketio.on("message_event")
def handle_message_event(json, methods=["GET","POST"]) -> None:
    print(f"Event received: {str(json)}")
    for message in json:
        chat_history.append(json[message])
    socketio.emit("my response", chat_history, callback=message_confirm)

def main() -> None:
    socketio.run(app, debug=True)

if __name__ == '__main__':
    main()
