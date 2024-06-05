# backend_connectify/backend/models/chatroom.py
#!/usr/bin/python3

"""
Chatroom Module
===============

This module defines the Chatroom class, which represents a chatroom in the
database. The Chatroom class inherits from BaseModel and Base, providing
attributes and relationships specific to a chatroom.

Classes:
--------
    Chatroom: A class to manage chatroom information.

Usage:
------
    from models.chatroom import Chatroom
    new_chatroom = Chatroom(name="General", user_id="user1234")
    new_chatroom.save()
"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Chatroom(BaseModel, Base):
    """
    Representation of a chatroom.

    Attributes:
    -----------
        __tablename__ (str): The name of the MySQL table to store chatrooms.
        name (sqlalchemy.String): The name of the chatroom, cannot be null.
        user_id (sqlalchemy.String): The ID of the user who created the chatroom, cannot be null.
        conversations (sqlalchemy.orm.relationship): Relationship to the Conversation class, cascading all deletions.
    """
    #if models.storage_t == 'db'

    __tablename__ = 'chatrooms'
    name = Column(String(128), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    conversations = relationship("Conversation", backref="chatroom", cascade="all, delete")
    '''
    else:
        name = ""
        user_id = ""
        conversations = []
    '''
    def __init__(self, *args, **kwargs):
        """
        Initializes a Chatroom instance.

        Args:
        -----
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments, typically including:
                - name (str): The name of the chatroom.
                - user_id (str): The ID of the user who created the chatroom.

        Attributes:
        -----------
            name (str): The name of the chatroom.
            user_id (str): The ID of the user who created the chatroom.
        """
        super().__init__(*args, **kwargs)
        if models.storage_t != 'db':
            self.name = kwargs.get('name', "")
            self.user_id = kwargs.get('user_id', "")
