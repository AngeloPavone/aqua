from datetime import datetime
from flask import Flask, render_template, request


app = Flask("aqua")


@app.route("/")
def home() -> object:
    """docstring"""
    return render_template("index.html", name="Angelo")


@app.route("/form-handler", methods=["GET", "POST"])
def handle_data() -> None:
    """docstring"""
    print(request.form["chat"])
    now = datetime.now()
    time = now.strftime("%H:%M  %m/%d/%Y") # Get date and time of request

    chat_log = open("chat-log.txt", "a", encoding="utf8") # open text file and save data from form
    chat_log.write(request.form['chat'] + " " + time + "\n")
    chat_log.close()

    return render_template('index.html', name="Input recieved")

def main() -> None:
    """docstring"""
    app.run(debug=True)


if __name__ == '__main__':
    main()
