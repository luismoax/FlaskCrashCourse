from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello():
    return "Hello World"

@app.route('/fuck/<name>')
def fuck(name):
    return 'Fucking testing' + ' ' + str(name)


if __name__ == "__main__":
    app.run(debug=True)