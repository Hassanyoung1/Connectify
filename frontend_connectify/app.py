# frontend_connectify/app.py
import os
from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, storage
import spotipy
import spotipy.oauth2 as oauth2

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')
Bootstrap(app)

# Initialize Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Define the Spotify client credentials
SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")

# Define the Spotify API object
sp = None

# Define the Spotify OAuth object
oauth = oauth2.SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=None,
    scope="playlist-modify-public,playlist-modify-private,playlist-modify-public,playlist-modify-private,streaming"
)

# Define the Spotify API object
sp = spotipy.Spotify(auth_manager=oauth)

# Configure Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return storage.get(User, user_id)

# Define the Flask routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Handle registration request
        username = request.json.get("username")
        email = request.json.get("email")
        password = request.json.get("password")

        # Check if the username or email already exists
        existing_user = storage.all(User).values()
        if any(user.username == username or user.email == email for user in existing_user):
            return jsonify({'error': 'Username or email already exists'}), 400

        # Create a new User instance
        password_hash = generate_password_hash(password)
        user = User(username=username, email=email, password_hash=password_hash)

        # Save the user instance to the storage
        storage.new(user)
        storage.save()

        return jsonify({'message': 'Registration successful'}), 201

    return render_template("Reg_page/reg.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Handle login request
        email = request.json.get("email")
        password = request.json.get("password")

        # Find the user by email
        user = next((user for user in storage.all(User).values() if user.email == email), None)

        if user and check_password_hash(user.password_hash, password):
            # Log in the user
            login_user(user)
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'error': 'Invalid email or password'}), 401

    return render_template("Login_page/login.html")

@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful'}), 200

@app.route("/profile")
@login_required
def profile():
    return render_template("user_profile_page/index.html")

@app.route("/chat")
@login_required
def chat():
    return render_template("user_profile_page/chat.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_term = request.form.get("search_term")
        if search_term:
            # Perform the search using the Spotify API
            results = sp.search(search_term, type="track,artist,album")
            return render_template("search.html", results=results)
    return render_template("search.html")

@app.route("/play", methods=["GET", "POST"])
def play():
    if request.method == "POST":
        search_term = request.form.get("search_term")
        if search_term:
            # Perform the search using the Spotify API
            results = sp.search(search_term, type="track,artist,album")
            return render_template("play.html", results=results)
    return render_template("play.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5010, debug=True)