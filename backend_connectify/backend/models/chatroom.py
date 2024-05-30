# backend_connectify/backend/models/chatroom.py
#!/usr/bin/python3
""" holds class Chatroom"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Chatroom(BaseModel, Base):
    """Representation of a chatroom"""
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
        """Initializes Chatroom"""
        super().__init__(*args, **kwargs)
        if models.storage_t != 'db':
            self.name = kwargs.get('name', "")
            self.user_id = kwargs.get('user_id', "")
