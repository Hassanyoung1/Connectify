# backend_connectify/backend/models/playlist.py
#!/usr/bin/python3
"""
Playlist Module
===============

This module defines the Playlist class, which represents a playlist in the
database. The Playlist class inherits from BaseModel and Base, providing
attributes and relationships specific to a playlist.

Classes:
--------
    Playlist: A class to manage playlist information.

Usage:
------
    from models.playlist import Playlist
    new_playlist = Playlist(name="My Playlist", user_id="user1234")
    new_playlist.save()
"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


# if models.storage_t == 'db'

class Playlist(BaseModel, Base):
    """Representation of a playlist"""
    __tablename__ = 'playlists'       
    name = Column(String(128), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    tracks = relationship("Track", backref="playlist")
    """ 
    else:
        name = None
        user_id = ""
        tracks = []
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a Playlist instance.

        Args:
        -----
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments, typically including:
                - name (str): The name of the playlist.
                - user_id (str): The ID of the user who created the playlist.

        Attributes:
        -----------
            name (str): The name of the playlist.
            user_id (str): The ID of the user who created the playlist.
        """
        super().__init__(*args, **kwargs)
        if models.storage_t != 'db':
            self.name = kwargs.get('name', None)
