# backend_connectify/backend/models/playlist.py
#!/usr/bin/python3
""" holds class Playlist"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Playlist(BaseModel, Base):
    """Representation of a playlist"""
    if models.storage_t == 'db':
        __tablename__ = 'playlists'
        name = Column(String(128), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        tracks = relationship("Track", backref="playlist")
    else:
        name = None
        user_id = ""
        tracks = []

    def __init__(self, *args, **kwargs):
        """Initializes Playlist"""
        super().__init__(*args, **kwargs)
        if models.storage_t != 'db':
            self.name = kwargs.get('name', None)
