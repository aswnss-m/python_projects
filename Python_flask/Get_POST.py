from flask import Flask
app = Flask(__name__)

@app.route('/home')
@app.route('/')

def home():
    return "Welcome"

# Specifying the methodes of a page
@app.route('/onlypost', methods=['POST'])
def post_req():
    return "This page only allow post" # This will not show anyway

if __name__ == "__main__":
    app.run(debug=True)
