# backend_connectify/backend/models/user.py
#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5

class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        username = Column(String(128), nullable=False, unique=True)
        email = Column(String(128), nullable=False, unique=True)
        password_hash = Column(String(128), nullable=False)
        playlists = relationship("Playlist", backref="user", cascade="all, delete")
        chatrooms = relationship("Chatroom", backref="user", cascade="all, delete")
        sessions = relationship("Session", backref="user", cascade="all, delete")
    else:
        username = ""
        email = ""
        password_hash = ""
        playlists = []
        chatrooms = []
        sessions = []

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
        if models.storage_t != 'db':
            self.username = kwargs.get('username', "")
            self.email = kwargs.get('email', "")
            self.password_hash = kwargs.get('password_hash', "")
        self.password_hash = md5(self.password_hash.encode()).hexdigest()
