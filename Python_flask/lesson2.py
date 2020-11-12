from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello():
    return "Hello world"

# Getting the datas from url
@app.route('/home/<string:name>')
def hello_name(name):
    return "Hi, " + name

@app.route('/index')
def index():
    return open("index.html","r")

if __name__ == "__main__":
    app.run(debug=True)