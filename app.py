from flask import Flask, render_template
app = Flask(__name__)

@app.route("/home/")
@app.route("/index/")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login/")
def login():
    return render_template('login.html')

@app.route("/sign_in/")
def sign():
    return render_template('sign_in.html')

@app.route("/username/")
def username():
    return 'username'

@app.route("/favorites/")
def favorites():
    return 'favorites'

if __name__ == '__main__':
    app.run(debug=True)

