from flask import Flask, render_template


app = Flask('aqua')


@app.route('/')
def home():
    return render_template('index.html', name='Angelo')


def main():
    home()

    app.run(debug=True)


if __name__ == '__main__':
    main()
