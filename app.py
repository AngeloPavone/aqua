from datetime import datetime
from flask_socketio import SocketIO
from flask import Flask, render_template, request


app = Flask("aqua")
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route("/")
def home() -> object:
    """starts the home page"""
    return render_template("index.html")

@app.route("/form_handler", methods=["GET", "POST"])
def handle_data() -> None:
    """store chat into a text file"""
    now = datetime.now()
    time = now.strftime("%H:%M  %m/%d/%Y") # Get date and time of request.
    with open("chat_log.txt", "a", encoding="utf8") as chat_log: # Open text file and save data from form.
        chat_log.write(request.form['chat'] + " " + time + "\n")
    
    return render_template("index.html")

def main() -> None:
    """start socketio"""
    socketio.run(app, debug=True)


if __name__ == '__main__':
    main()