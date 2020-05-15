from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home/users/<string:name>/posts/<int:id>')
def hello(id = -1, name = 'default'):
    return "Hello, " + name + " your id is: " + str(id)

@app.route('/onlyget', methods = ['GET']) 
def get_req():
    return "You can only get this webpage."

@app.route('/onlypost', methods = ['POST'])
def only_post():
    return "This won't be displayed"

if __name__ == "__main__":
    app.run(debug=True)