# backend_connectify/backend/models/album.py
#!/usr/bin/python3
""" holds class Album"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Album(BaseModel, Base):
    """Representation of an album"""
 #   if models.storage_t == 'db'
    __tablename__ = 'albums'
    name = Column(String(128), nullable=False)
    artist = Column(String(128), nullable=False)
    release_year = Column(Integer, nullable=True)
    tracks = relationship("Track", back_populates="album", cascade="all, delete")
    '''
    else:
        name = ""
        artist = ""
        release_year = None
        tracks = []
    '''
    def __init__(self, *args, **kwargs):
        """Initializes Album"""
        super().__init__(*args, **kwargs)
        if models.storage_t != 'db':
            self.name = kwargs.get('name', "")
            self.artist = kwargs.get('artist', "")
            self.release_year = kwargs.get('release_year', None)
