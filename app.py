from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home/users/<string:name>/posts/<int:id>')
def hello(id, name):
    return "Hello, " + name + "your id is: " + str(id)

if __name__ == "__main__":
    app.run(debug=True)