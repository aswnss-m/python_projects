from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# * Initialising Flask , connecting Database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

#* Database object
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

@app.route('/posts', methods= ['GET', 'POST'])
def posts():
    
    
    return render_template("posts.html")

if __name__ == "__main__":
    app.run(debug=True)