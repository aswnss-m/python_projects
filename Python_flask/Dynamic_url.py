from flask import Flask

app = Flask(__name__)

# Setting up the home
@app.route('/')
@app.route('/home')
def hello():
    return "Hello world"

#! Dynamic URL

# Getting the datas from url   
@app.route('/home/<string:name>')
def hello_name(name):
    return "Hi, " + name

# Getting multiple data from url
@app.route('/home/<string:name>/<int:id>')
def get_id(name,id):
    return "welcome " + name + " id : " + str(id)



if __name__ == "__main__":
    app.run(debug=True)