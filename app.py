from flask import Flask
app = Flask(__name__)
# This is our basic route
@ app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# A route about us
@app.route("/about")
def about():
    return '''
    <h1>About</h1>
    <p>I learn Flask framework</p>
    '''
# Dynamic URL
@app.route("/user/<username>")
def shall_user(username):
    return f"<p>User profile: {username}</p>"
# A route with form processing
@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get