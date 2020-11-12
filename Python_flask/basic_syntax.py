from flask import Flask

app = Flask(__name__)   #! This is the syntax for making a Flask object


@app.route('/') # ? This decorator specify the loction of the below function : www.yourdoamin.com/
@app.route('/home')
def hello():
    return "Hello World"

# TODO: I have to understand what this is
if __name__ == '__main__':
    app.run(debug=True)


