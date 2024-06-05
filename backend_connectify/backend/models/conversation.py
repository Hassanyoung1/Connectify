# backend_connectify/backend/models/conversation.py
#!/usr/bin/python3
"""
Conversation Module
===================

This module defines the Conversation class, which represents a conversation in the
database. The Conversation class inherits from BaseModel and Base, providing
attributes specific to a conversation.

Classes:
--------
    Conversation: A class to manage conversation information.

Usage:
------
    from models.conversation import Conversation
    new_conversation = Conversation(message="", user_id="", chatroom_id="")
    new_conversation.save()
"""


import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Conversation(BaseModel, Base):
    """
    Representation of a conversation.

    Attributes:
    -----------
        __tablename__ (str): The name of the MySQL table to store conversations.
        message (sqlalchemy.String): The message content of the conversation, cannot be null.
        user_id (sqlalchemy.String): The ID of the user who sent the message, cannot be null.
        chatroom_id (sqlalchemy.String): The ID of the chatroom where the conversation took place, cannot be null.
    """

    #if models.storage_t == 'db'
    __tablename__ = 'conversations'
    message = Column(String(256), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    chatroom_id = Column(String(60), ForeignKey('chatrooms.id'), nullable=False)
    '''
    else:
        message = ""
        user_id = ""
        chatroom_id = ""
    '''
    def __init__(self, *args, **kwargs):
        """
        Initializes a Conversation instance.

        Args:
        -----
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments, typically including:
                - message (str): The message content of the conversation.
                - user_id (str): The ID of the user who sent the message.
                - chatroom_id (str): The ID of the chatroom where the conversation took place.

        Attributes:
        -----------
            message (str): The message content of the conversation.
            user_id (str): The ID of the user who sent the message.
            chatroom_id (str): The ID of the chatroom where the conversation took place.
        """
        super().__init__(*args, **kwargs)
        if models.storage_t != 'db':
            self.message = kwargs.get('message', "")
            self.user_id = kwargs.get('user_id', "")
            self.chatroom_id = kwargs.get('chatroom_id', "")
