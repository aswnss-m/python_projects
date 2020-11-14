from flask import Flask, render_template
from datetime import datetime
#? Importing the alchemy , this is used to connect to database
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# TODO : we need to specify the name of the external database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'   
# * database///<relative filepath to save>
# * database////<absolutepath filepath to save>

db = SQLAlchemy(app)    #! Connecting database

# TODO This is the table
class BlogPost(db.Model):
    
    #TODO : Creating Columns in the database
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable= False)
    author = db.Column(db.String(32), nullable = False, default= 'N/A')
    date_posted =db.Column(db.DateTime, nullable=False, default= datetime.utcnow)

    # * Printing the ID , each time a BlogPost is creating
    def __repr__(self):
        return 'Blog post ' + str(self.id)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)