from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home/<string:name>')
def hello(name = 'def'):
    return "Hello, " + name

if __name__ == "__main__":
    app.run(debug=True)