# backend_connectify/backend/models/session.py
#!/usr/bin/python3
"""
Session Module
==============

This module defines the Session class, which represents a session in the
database. The Session class inherits from BaseModel and Base, providing
attributes specific to a session.

Classes:
--------
    Session: A class to manage session information.

Usage:
------
    from models.session import Session
    new_session = Session(session_id="session1234", user_id="user5678")
    new_session.save()
"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
 # if models.storage_t == 'db':
class Session(BaseModel, Base):
    """Representation of a session"""
   
    __tablename__ = 'sessions'
    session_id = Column(String(128), nullable=False, unique=True)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    
    ''' else:
        session_id = ""
        user_id = ""
'''

    def __init__(self, *args, **kwargs):
        """
        Initializes a Session instance.

        Args:
        -----
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments, typically including:
                - session_id (str): The unique identifier for the session.
                - user_id (str): The ID of the user associated with the session.

        Attributes:
        -----------
            session_id (str): The unique identifier for the session.
            user_id (str): The ID of the user associated with the session.
        """
        super().__init__(*args, **kwargs)
        if models.storage_t != 'db':
            self.session_id = kwargs.get('session_id', "")
            self.user_id = kwargs.get('user_id', "")
