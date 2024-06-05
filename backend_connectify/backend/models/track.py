# backend_connectify/backend/models/track.py
#!/usr/bin/python3
"""
Track Module
============

This module defines the Track class, which represents a track in the
database. The Track class inherits from BaseModel and Base, providing
attributes and relationships specific to a track.

Classes:
--------
    Track: A class to manage track information.

Usage:
------
    from models.track import Track
    new_track = Track(name="Song Title", artist="Artist Name", duration=180, playlist_id="playlist1234")
    new_track.save()
"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

class Track(BaseModel, Base):
    """
    Representation of a track.

    Attributes:
    -----------
        __tablename__ (str): The name of the MySQL table to store tracks.
        name (sqlalchemy.String): The name of the track, cannot be null.
        artist (sqlalchemy.String): The artist of the track, cannot be null.
        album_id (sqlalchemy.String): The ID of the album to which the track belongs, nullable.
        duration (sqlalchemy.Integer): The duration of the track in seconds, cannot be null.
        spotify_id (sqlalchemy.String): The Spotify ID of the track, nullable.
        spotify_url (sqlalchemy.String): The Spotify URL of the track, nullable.
        rating (sqlalchemy.Float): The rating of the track, nullable.
        playlist_id (sqlalchemy.String): The ID of the playlist to which the track belongs, cannot be null.
        album (sqlalchemy.orm.relationship): Relationship to the Album class.
    """

#    if models.storage_t == 'db'
    __tablename__ = 'tracks'
    name = Column(String(128), nullable=False)
    artist = Column(String(128), nullable=False)
    album_id = Column(String(60), ForeignKey('albums.id'), nullable=True)
    duration = Column(Integer, nullable=False)
    spotify_id = Column(String(128), nullable=True)
    spotify_url = Column(String(256), nullable=True)
    rating = Column(Float, nullable=True)
    playlist_id = Column(String(60), ForeignKey('playlists.id'), nullable=False)
    album = relationship("Album", back_populates="tracks")
    '''
    else:
        name = ""
        artist = ""
        album_id = ""
        duration = None
        spotify_id = ""
        spotify_url = ""
        rating = None
        playlist_id = ""
    '''
    def __init__(self, *args, **kwargs):
        """
        Initializes a Track instance.

        Args:
        -----
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments, typically including:
                - name (str): The name of the track.
                - artist (str): The artist of the track.
                - album_id (str): The ID of the album to which the track belongs.
                - duration (int): The duration of the track in seconds.
                - spotify_id (str): The Spotify ID of the track.
                - spotify_url (str): The Spotify URL of the track.
                - rating (float): The rating of the track.
                - playlist_id (str): The ID of the playlist to which the track belongs.

        Attributes:
        -----------
            name (str): The name of the track.
            artist (str): The artist of the track.
            album_id (str): The ID of the album to which the track belongs.
            duration (int): The duration of the track in seconds.
            spotify_id (str): The Spotify ID of the track.
            spotify_url (str): The Spotify URL of the track.
            rating (float): The rating of the track.
            playlist_id (str): The ID of the playlist to which the track belongs.
        """

        super().__init__(*args, **kwargs)
        if models.storage_t != 'db':
            self.name = kwargs.get('name', "")
            self.artist = kwargs.get('artist', "")
            self.album_id = kwargs.get('album_id', "")
            self.duration = kwargs.get('duration', None)
            self.playlist_id = kwargs.get('playlist_id', "")
