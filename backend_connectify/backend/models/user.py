#!/usr/bin/python3
"""
User Module
===========

This module defines the User class, which represents a user in the database.
The User class inherits from BaseModel, Base, and SQLAlchemyUserMixin, providing
attributes and methods specific to a user.

Classes:
--------
    SQLAlchemyUserMixin: A mixin class for SQLAlchemy user model to integrate with Flask-Login.
    User: A class to manage user information.

Usage:
------
    from models.user import User
    new_user = User(username="example_user", email="user@example.com")
    new_user.save()
"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from flask_login import UserMixin
import bcrypt 



class SQLAlchemyUserMixin(UserMixin):
    """
    Mixin for SQLAlchemy user model to integrate with Flask-Login.

    Attributes:
    -----------
        is_active (bool): Indicates if the user account is active.
        is_authenticated (bool): Indicates if the user is authenticated.
        is_anonymous (bool): Indicates if the user is an anonymous user.
    """

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

class User(BaseModel, Base, SQLAlchemyUserMixin):
     """
    Representation of a user.

    Attributes:
    -----------
        __tablename__ (str): The name of the MySQL table to store users.
        username (sqlalchemy.String): The username of the user, cannot be null and must be unique.
        email (sqlalchemy.String): The email address of the user, cannot be null and must be unique.
        password_hash (sqlalchemy.Text): The hashed password of the user, nullable.
        playlists (sqlalchemy.orm.relationship): Relationship to the Playlist class.
        chatrooms (sqlalchemy.orm.relationship): Relationship to the Chatroom class.
        sessions (sqlalchemy.orm.relationship): Relationship to the Session class.
    """
 #   if models.storage_t == 'db':
    __tablename__ = 'users'
    username = Column(String(128), nullable=False, unique=True)
    email = Column(String(128), nullable=False, unique=True)
    password_hash = Column(Text, nullable=True)
    playlists = relationship("Playlist", backref="user", cascade="all, delete")
    chatrooms = relationship("Chatroom", backref="user", cascade="all, delete")
    sessions = relationship("Session", backref="user", cascade="all, delete")
    '''
    else:
        username = ""
        email = ""
        password_hash = ""
        playlists = []
        chatrooms = []
        sessions = []
    '''
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username = kwargs.get('username', "")
        self.email = kwargs.get('email', "")
    #   salt = bcrypt.gensalt()
    #   self.password_hash = bcrypt.hashpw(kwargs.get('password', "").encode("utf-8"), salt)

    def check_password(self, password):
        """Check hashed password."""
        return bcrypt.checkpw(password.encode("utf-8"), self.password_hash.encode('utf-8')) 

# Add Flask-Login functionality separately using composition
class UserWithLogin(User, SQLAlchemyUserMixin):
    pass
