# backend_connectify/backend/models/album.py
#!/usr/bin/python3
"""
Album Module
============

This module defines the Album class, which represents an album in the
database. The Album class inherits from BaseModel and Base, providing
attributes and relationships specific to an album.

Classes:
--------
    Album: A class to manage album information.

Usage:
------
    from models.album import Album
    new_album = Album(name="Album Name", artist="Artist Name", release_year=)
    new_album.save()
"""


import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Album(BaseModel, Base):
    """
    Representation of an album.

    Attributes:
    -----------
        __tablename__ (str): The name of the MySQL table to store albums.
        name (sqlalchemy.String): The name of the album, cannot be null.
        artist (sqlalchemy.String): The artist of the album, cannot be null.
        release_year (sqlalchemy.Integer): The release year of the album, can be null.
        tracks (sqlalchemy.orm.relationship): Relationship to the Track class, cascading all deletions.
    """

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
        """
        Initializes an Album instance.

        Args:
        -----
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments, typically including:
                - name (str): The name of the album.
                - artist (str): The artist of the album.
                - release_year (int): The release year of the album.

        Attributes:
        -----------
            name (str): The name of the album.
            artist (str): The artist of the album.
            release_year (int): The release year of the album.
        """

        super().__init__(*args, **kwargs)
        if models.storage_t != 'db':
            self.name = kwargs.get('name', "")
            self.artist = kwargs.get('artist', "")
            self.release_year = kwargs.get('release_year', None)
