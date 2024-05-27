# backend_connectify/backend/models/session.py
#!/usr/bin/python3
""" holds class Session"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Session(BaseModel, Base):
    """Representation of a session"""
    if models.storage_t == 'db':
        __tablename__ = 'sessions'
        session_id = Column(String(128), nullable=False, unique=True)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        session_id = ""
        user_id = ""

    def __init__(self, *args, **kwargs):
        """Initializes Session"""
        super().__init__(*args, **kwargs)
        if models.storage_t != 'db':
            self.session_id = kwargs.get('session_id', "")
            self.user_id = kwargs.get('user_id', "")
