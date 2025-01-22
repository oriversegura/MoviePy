from flask import Flask, render_template, request, url_for, flash, redirect
import handlers.users

app = Flask(__name__)

app.static_folder = 'static'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup", methods=('GET', 'POST'))

def signup():
    if request.method == 'POST':
        mail = request.form['mail']
        
        if not mail:
            flash('Title is required!')

        else:
            return redirect(url_for('login'))
    
    return render_template("signup.html")

@app.route("/movies")
def movies():
    return render_template("movies.html")


if __name__== '__main__':
    app.run(debug=True)
    