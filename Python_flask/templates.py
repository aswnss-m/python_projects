''' 
Templates are html files.
Inorder for flask to render them , they must be stored inside a folder templates
'''

from flask import Flask, render_template    #? render_template is used to render html files
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True) 