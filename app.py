from datetime import datetime
from time import time
from flask import Flask, request, redirect
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts', methods=['GET', 'POST'])
def posts():    
    # if is a post request
    if request.method == 'POST':        
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        
        # create the object
        new_post = BlogPost(title = post_title, content = post_content, author = post_author)
        # add to the db
        db.session.add(new_post)
        # commit the change
        db.session.commit()
        return redirect('/posts')
    else:
        # get all posts added so far
        added_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        
        return render_template('posts.html', posts = added_posts)
        

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