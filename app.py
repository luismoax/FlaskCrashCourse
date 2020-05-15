from datetime import datetime
from time import time
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///posts.db"
db = SQLAlchemy(app)

# designing the model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    author = db.Column(db.String(50), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return 'Blog Post ' + str(self.id)


all_posts = [
    {
        'title': 'Amorphis Post',
        'content': 'This is the content of post 1',
        'author': 'Luismo'
    },
    {
        'title': 'In Flames Post',
        'content': 'Testing this awesome micro-framework'
    },
    {
        'title': 'Lorem Post',
        'content': '''Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                      Aliquid voluptatum quia quaerat necessitatibus fugiat tenetur nostrum! 
                      Suscipit sapiente quam quia. Repudiandae eos, cumque quas 
                      atque aut amet corporis distinctio enim.'''
    }
]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts = all_posts)

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