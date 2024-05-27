# backend_connectify/backend/models/track.py
#!/usr/bin/python3
""" holds class Track"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

class Track(BaseModel, Base):
    """Representation of a track"""
    if models.storage_t == 'db':
        __tablename__ = 'tracks'
        name = Column(String(128), nullable=False)
        artist = Column(String(128
), nullable=False)
        album_id = Column(String(60), ForeignKey('albums.id'), nullable=True)
        duration = Column(Integer, nullable=False)
        spotify_id = Column(String(128), nullable=True)
        spotify_url = Column(String(256), nullable=True)
        rating = Column(Float, nullable=True)
        playlist_id = Column(String(60), ForeignKey('playlists.id'), nullable=False)
        album = relationship("Album", back_populates="tracks")
    else:
        name = ""
        artist = ""
        album_id = ""
        duration = None
        spotify_id = ""
        spotify_url = ""
        rating = None
        playlist_id = ""

    def __init__(self, *args, **kwargs):
        """Initializes Track"""
        super().__init__(*args, **kwargs)
        if models.storage_t != 'db':
            self.name = kwargs.get('name', "")
            self.artist = kwargs.get('artist', "")
            self.album_id = kwargs.get('album_id', "")
            self.duration = kwargs.get('duration', None)
            self.playlist_id = kwargs.get('playlist_id', "")
