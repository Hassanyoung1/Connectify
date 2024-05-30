from flask import Flask, jsonify, request, render_template, redirect, url_for 
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from models import storage
from models.user import User, UserWithLogin
from models.playlist import Playlist
from models.track import Track
from models.album import Album
from models.chatroom import Chatroom
from models.conversation import Conversation
from models.session import Session
from dotenv import load_dotenv, find_dotenv
import bcrypt 

'''from routes.spotify_api import spotify_api'''
from flask_bcrypt import Bcrypt

load_dotenv(find_dotenv())


app = Flask(__name__, template_folder='../../frontend_connectify/templates', static_folder='../../frontend_connectify/static')
app.config['SECRET_KEY'] = 'your_secret_key'

CORS(app)  # Enable CORS for all routes

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return storage.get(UserWithLogin, user_id)

@app.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('user_profile_page/index.html')
    else:
        return redirect(url_for('login'))  # Redirect to login page if not logged in

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('Reg_page/reg.html')
    
    data = request.get_json(silent=True)  
    if not data:  
        return jsonify({'error': 'No data sent'}), 400

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')

    if not all([username, email, password, confirm_password]):
        return jsonify({'error': 'Missing fields'}), 400

    if password != confirm_password:
        return jsonify({'error': 'Passwords do not match'}), 400

    existing_user = storage.all(UserWithLogin).values()
    if any(user.username == username or user.email == email for user in existing_user):
        return jsonify({'error': 'Username or email already exists'}), 400

#    password_hash = generate_password_hash(password)
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw((password).encode("utf-8"), salt)
    new_user = User(username=username, email=email, password_hash=password_hash)
    storage.new(new_user)
    storage.save()

    login_user(new_user)
    return jsonify({'message': "success!"}), 201

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('Login_page/login.html')

    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = next((u for u in storage.all(UserWithLogin).values() if u.email == email), None)
    
    if user and check_password_hash(user.password_hash, password):
        login_user(user)
        return redirect(url_for('index'))  # Redirect to user profile page after successful login
    else:
        return jsonify({'error': 'Invalid email or password'}), 401

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful'}), 200

# Playlist management routes
@app.route('/playlists', methods=['POST'])
@login_required
def create_playlist():
    name = request.json.get('name')

    # Create a new Playlist instance
    playlist = Playlist(name=name, user_id=current_user.id)

    # Save the playlist instance to the storage
    storage.new(playlist)
    storage.save()

    return jsonify({'message': 'Playlist created successfully', 'playlist_id': playlist.id}), 201

@app.route('/playlists/<playlist_id>', methods=['GET'])
@login_required
def get_playlist(playlist_id):
    # Retrieve the playlist instance from the storage
    playlist = storage.get(Playlist, playlist_id)

    if playlist:
        return jsonify(playlist.to_dict()), 200
    else:
        return jsonify({'error': 'Playlist not found'}), 404

@app.route('/playlists/<playlist_id>', methods=['PUT'])
@login_required
def update_playlist(playlist_id):
    name = request.json.get('name')

    # Retrieve the playlist instance from the storage
    playlist = storage.get(Playlist, playlist_id)

    if playlist:
        # Update the playlist name
        playlist.name = name
        storage.save()
        return jsonify({'message': 'Playlist updated successfully'}), 200
    else:
        return jsonify({'error': 'Playlist not found'}), 404

@app.route('/playlists/<playlist_id>', methods=['DELETE'])
@login_required
def delete_playlist(playlist_id):
    # Retrieve the playlist instance from the storage
    playlist = storage.get(Playlist, playlist_id)

    if playlist:
        # Delete the playlist instance from the storage
        storage.delete(playlist)
        storage.save()
        return jsonify({'message': 'Playlist deleted successfully'}), 200
    else:
        return jsonify({'error': 'Playlist not found'}), 404

# Other routes
@app.route('/playlists/<playlist_id>/tracks', methods=['POST'])
@login_required
def add_track_to_playlist(playlist_id):
    track_name = request.json.get('track_name')

    # Search for the track using the Spotify API
    track_info = search_track(track_name)

    if track_info:
        # Retrieve the playlist instance from the storage
        playlist = storage.get(Playlist, playlist_id)

        if playlist:
            # Create a new Track instance
            track = Track(
                name=track_info['name'],
                artist=track_info['artist'],
                spotify_id=track_info['id'],
                spotify_url=track_info['url'],
                playlist_id=playlist_id
            )

            # Save the track instance to the storage
            storage.new(track)
            storage.save()

            return jsonify({'message': 'Track added to playlist successfully'}), 201
        else:
            return jsonify({'error': 'Playlist not found'}), 404
    else:
        return jsonify({'error': 'Track not found'}), 404

@app.route('/playlists/<playlist_id>/tracks/<track_id>', methods=['DELETE'])
@login_required
def remove_track_from_playlist(playlist_id, track_id):
    # Retrieve the track instance from the storage
    track = storage.get(Track, track_id)

    if track:
        # Delete the track instance from the storage
        storage.delete(track)
        storage.save()
        return jsonify({'message': 'Track removed from playlist successfully'}), 200
    else:
        return jsonify({'error': 'Track not found'}), 404

# Chatroom management routes
@app.route('/chatrooms', methods=['POST'])
@login_required
def create_chatroom():
    name = request.json.get('name')

    # Create a new Chatroom instance
    chatroom = Chatroom(name=name, user_id=current_user.id)

    # Save the chatroom instance to the storage
    storage.new(chatroom)
    storage.save()

    return jsonify({'message': 'Chatroom created successfully', 'chatroom_id': chatroom.id}), 201

@app.route('/chatrooms/<chatroom_id>', methods=['GET'])
@login_required
def get_chatroom(chatroom_id):
    # Retrieve the chatroom instance from the storage
    chatroom = storage.get(Chatroom, chatroom_id)

    if chatroom:
        return jsonify(chatroom.to_dict()), 200
    else:
        return jsonify({'error': 'Chatroom not found'}), 404

@app.route('/chatrooms/<chatroom_id>', methods=['DELETE'])
@login_required
def delete_chatroom(chatroom_id):
    # Retrieve the chatroom instance from the storage
    chatroom = storage.get(Chatroom, chatroom_id)

    if chatroom:
        # Delete the chatroom instance from the storage
        storage.delete(chatroom)
        storage.save()
        return jsonify({'message': 'Chatroom deleted successfully'}), 200
    else:
        return jsonify({'error': 'Chatroom not found'}), 404

# Conversation management routes
@app.route('/chatrooms/<chatroom_id>/conversations', methods=['POST'])
@login_required
def create_conversation(chatroom_id):
    message = request.json.get('message')

    # Retrieve the chatroom instance from the storage
    chatroom = storage.get(Chatroom, chatroom_id)

    if chatroom:
        # Create a new Conversation instance
        conversation = Conversation(message=message, user_id=current_user.id, chatroom_id=chatroom_id)

        # Save the conversation instance to the storage
        storage.new(conversation)
        storage.save()

        return jsonify({'message': 'Conversation created successfully'}), 201
    else:
        return jsonify({'error': 'Chatroom not found'}), 404

@app.route('/chatrooms/<chatroom_id>/conversations', methods=['GET'])
@login_required
def get_conversations(chatroom_id):
    # Retrieve the chatroom instance from the storage
    chatroom = storage.get(Chatroom, chatroom_id)

    if chatroom:
        # Retrieve all conversations for the chatroom
        conversations = storage.all(Conversation).values()
        conversations = [conv.to_dict() for conv in conversations if conv.chatroom_id == chatroom_id]

        return jsonify(conversations), 200
    else:
        return jsonify({'error': 'Chatroom not found'}), 404

@app.route('/sessions', methods=['POST'])
@login_required
def create_session():
    playlist_id = request.json.get('playlist_id')
    chatroom_id = request.json.get('chatroom_id')
    # Retrieve the playlist and chatroom instances from the storage
    playlist = storage.get(Playlist, playlist_id)
    chatroom = storage.get(Chatroom, chatroom_id)
    if playlist and chatroom:
        # Create a new Session instance
        session = Session(playlist_id=playlist_id, chatroom_id=chatroom_id)
        # Save the session instance to the storage
        storage.new(session)
        storage.save()
        return jsonify({'message': 'Session created successfully', 'session_id': session.id}), 201
    else:
        return jsonify({'error': 'Playlist or chatroom not found'}), 404

@app.route('/sessions/<session_id>', methods=['GET'])
@login_required
def get_session(session_id):
    # Retrieve the session instance from the storage
    session = storage.get(Session, session_id)
    if session:
        return jsonify(session.to_dict()), 200
    else:
        return jsonify({'error': 'Session not found'}), 404

@app.route('/sessions/<session_id>', methods=['DELETE'])
@login_required
def delete_session(session_id):
    # Retrieve the session instance from the storage
    session = storage.get(Session, session_id)
    if session:
        # Delete the session instance from the storage
        storage.delete(session)
        storage.save()
        return jsonify({'message': 'Session deleted successfully'}), 200
    else:
        return jsonify({'error': 'Session not found'}), 404
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)