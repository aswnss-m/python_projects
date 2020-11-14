from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# * The data that needed to be passed is a list of dictionaries
all_posts = [
    {
        'title':'Post 1',
        'content':'This is the content for post 1.',
        'author':'Aswnss'
    },
    {
        'title':'Post 2',
        'content':'This is the content of post 2.'
    }
]


@app.route('/posts')
def posts():
    # ! Passing data to an html file is done using render_template
    # TODO render_template('<filename>', <variable_name> = <variable>)
    return render_template('posts.html', posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)