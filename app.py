import os
from datetime import *
from flask import Flask, request, redirect, render_template, url_for, session
from lib.user_repository import UserRepository
from lib.user import User
from lib.post_repository import PostRepository
from lib.post import Post
from lib.database_connection import get_flask_database_connection

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def restart_session():
    session.clear()

@app.route('/')
def get_index():
    connection = get_flask_database_connection(app)
    repository = PostRepository(connection)
    posts = repository.all()
    posts.reverse()
    
    # Check if the user is logged in
    logged_in = 'user_id' in session
    
    return render_template("index.html", posts=posts, logged_in=logged_in)

@app.route('/', methods=['POST'])
def post_index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    connection = get_flask_database_connection(app)
    repository = PostRepository(connection)
    
    content = request.form.get('content')
    user_id = session['user_id']

    if not content or not user_id:
        return "Bad Request: Missing fields", 400

    post = Post(None, content, None, user_id)
    post = repository.create(post)

    return redirect(url_for('get_index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        user = User(None,
                    request.form['username'],
                    request.form['email'],
                    request.form['password'])
        try:
            user = repository.create(user)
            return redirect(url_for('get_success'))
        except ValueError as e:
            error_message = str(e)
            return render_template('register.html', error_message=error_message)
    return render_template('register.html')

@app.route('/success')
def get_success():
    return render_template('success.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        connection = get_flask_database_connection(app)
        user_repository = UserRepository(connection)
        
        user = user_repository.find_by_email_and_password(email, password)
        if user:
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('get_index'))
        else:
            return "Invalid credentials", 401

    return render_template('login.html')

@app.route('/logout')
def logout():
    restart_session()
    return redirect(url_for('get_index'))

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))