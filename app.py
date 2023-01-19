from flask import Flask, render_template, request
from datetime import datetime


app = Flask('aqua')


@app.route('/')
def home():
    return render_template('index.html', name='Angelo')


@app.route('/form-handler', methods=['GET', 'POST'])
def handle_data():
    print(request.form['chat'])
    now = datetime.now()
    time = now.strftime("%H:%M  %m/%d/%Y") #Get date and time of request


    chatLog = open("chat-log.txt", 'a') #open text file and save data from form
    chatLog.write(request.form['chat'] + " " + time + "\n")
    chatLog.close()

    return render_template('index.html', name="Input recieved")

def main():
    home()

    app.run(debug=True)


if __name__ == '__main__':
    main()
