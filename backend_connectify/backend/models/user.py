#!/usr/bin/python3
""" holds class User"""
'''from app import bcrypt'''
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from flask_login import UserMixin
import bcrypt 



class SQLAlchemyUserMixin(UserMixin):
    """Mixin for SQLAlchemy user model to integrate with Flask-Login"""
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
    """Representation of a user """
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
