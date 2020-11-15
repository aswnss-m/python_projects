from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# * Initialising Flask , connecting Database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

#* Database object , passing the flask object
db = SQLAlchemy(app)

#* Structuring the Database
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(32),nullable=False,default='N/A')
    date_posted = db.Column(db.DateTime,nullable = False, default=datetime.utcnow)

    def __repr__(self):
        return "Post No. " + str(self.id)




#* Connecting the html files with flask
@app.route('/')
@app.route('/home')
def home():
    
    return render_template("index.html")

# * Adding the method post to integrate with database : default is 'get' only
@app.route('/posts', methods= ['GET', 'POST'])
def posts():

    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']

        new_post = BlogPost(title =post_title,content =post_content,author=post_author)

        db.session.add(new_post)
        db.session.commit()
        
        #* Refreshing the page to show the db update
        return redirect('/posts')
    
    #* This runs at the start , getting previous datas from db
    else:

        all_posts = BlogPost.query.order_by(BlogPost.date_posted)
        return render_template("posts.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)