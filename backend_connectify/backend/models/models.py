#!/usr/bin/python3
from models.engine.db_storage import db
from models.base_model import BaseModel

class Playlist(db.Model, BaseModel):
    """Representation of a playlist"""
    __tablename__ = 'playlists'
    id = db.Column(db.String(60), primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    tracks = db.relationship("Track", backref="playlist", cascade="all, delete")

class Track(db.Model, BaseModel):
    """Representation of a track"""
    __tablename__ = 'tracks'
    id = db.Column(db.String(60), primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    artist = db.Column(db.String(128), nullable=False)
    album_id = db.Column(db.String(60), db.ForeignKey('albums.id'), nullable=True)
    duration = db.Column(db.Integer, nullable=False)
    spotify_id = db.Column(db.String(128), nullable=True)
    spotify_url = db.Column(db.String(256), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    playlist_id = db.Column(db.String(60), db.ForeignKey('playlists.id'), nullable=False)
    album = db.relationship("Album", back_populates="tracks")

class Album(db.Model, BaseModel):
    """Representation of an album"""
    __tablename__ = 'albums'
    id = db.Column(db.String(60), primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    artist = db.Column(db.String(128), nullable=False)
    release_year = db.Column(db.Integer, nullable=True)
    tracks = db.relationship("Track", back_populates="album", cascade="all, delete")

class Chatroom(db.Model, BaseModel):
    """Representation of a chatroom"""
    __tablename__ = 'chatrooms'
    id = db.Column(db.String(60), primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    conversations = db.relationship("Conversation", backref="chatroom", cascade="all, delete")

class Conversation(db.Model, BaseModel):
    """Representation of a conversation"""
    __tablename__ = 'conversations'
    id = db.Column(db.String(60), primary_key=True)
    message = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    chatroom_id = db.Column(db.String(60), db.ForeignKey('chatrooms.id'), nullable=False)

class Session(db.Model, BaseModel):
    """Representation of a session"""
    __tablename__ = 'sessions'
    id = db.Column(db.String(60), primary_key=True)
    playlist_id = db.Column(db.String(60), db.ForeignKey('playlists.id'), nullable=False)
    chatroom_id = db.Column(db.String(60), db.ForeignKey('chatrooms.id'), nullable=False)