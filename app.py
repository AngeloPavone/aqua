from datetime import datetime
from flask_socketio import SocketIO
from flask import Flask, render_template, request


app = Flask("aqua")
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route("/")
def home() -> object:
    """docstring"""
    return render_template("index.html", name="Aqua")

@app.route("/form-handler", methods=["GET", "POST"])
def handle_data() -> None:
    """docstring"""
    now = datetime.now()
    time = now.strftime("%H:%M  %m/%d/%Y") # Get date and time of request
    with open("chat-log.txt", "a", encoding="utf8") as f: # open text file and save data from form
        f.write(request.form['chat'] + " " + time + "\n")

    with open("chat-log.txt", "r", encoding="utf8") as f:
        lines = f.readlines()


    return render_template("index.html", content=lines)

def main() -> None:
    """docstring"""
    pass


if __name__ == '__main__':
    socketio.run(app)
    main()