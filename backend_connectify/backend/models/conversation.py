# backend_connectify/backend/models/conversation.py
#!/usr/bin/python3
""" holds class Conversation"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Conversation(BaseModel, Base):
    """Representation of a conversation"""
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
        """Initializes Conversation"""
        super().__init__(*args, **kwargs)
        if models.storage_t != 'db':
            self.message = kwargs.get('message', "")
            self.user_id = kwargs.get('user_id', "")
            self.chatroom_id = kwargs.get('chatroom_id', "")
