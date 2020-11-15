from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
data =['Name','Branch','Physics','Chemistry','Maths','Language','Computer']

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///marksheet.db'

db =SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    Name = db.Column(db.String(32), nullable=False)
    Branch = db.Column(db.String(32), nullable=False, default= 'N/A')
    Physics = db.Column(db.Float,nullable =False, default = 0)
    Chemistry = db.Column(db.Float, nullable= False, default = 0)
    Maths = db.Column(db.Float, nullable= False, default = 0)
    Language = db.Column(db.Float, nullable= False, default = 0)
    Computer = db.Column(db.Float, nullable= False, default = 0)

@app.route('/')
@app.route('/home', methods=['GET','POST'])
def home():
    return render_template("index.html", details=data)
    # return "This works"
    

if __name__ == "__main__":

    app.run(debug=True)