# backend_connectify/backend/models/engine/db_storage.py
#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.user import User
from models.playlist import Playlist
from models.track import Track
from models.album import Album
from models.chatroom import Chatroom
from models.conversation import Conversation
from models.session import Session
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"User": User, "Playlist": Playlist, "Track": Track, "Album": Album, "Chatroom": Chatroom, "Conversation": Conversation, "Session": Session}

class DBStorage:
    """Interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        CONNECTIFY_MYSQL_USER = getenv('CONNECTIFY_MYSQL_USER')
        CONNECTIFY_MYSQL_PWD = getenv('CONNECTIFY_MYSQL_PWD')
        CONNECTIFY_MYSQL_HOST = getenv('CONNECTIFY_MYSQL_HOST')
        CONNECTIFY_MYSQL_DB = getenv('CONNECTIFY_MYSQL_DB')
        CONNECTIFY_ENV = getenv('CONNECTIFY_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(CONNECTIFY_MYSQL_USER,
                                             CONNECTIFY_MYSQL_PWD,
                                             CONNECTIFY_MYSQL_HOST,
                                             CONNECTIFY_MYSQL_DB))
        if CONNECTIFY_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()

    def get(self, cls, id):
        """Retrieve one object"""
        try:
            return self.__session.query(cls).filter(cls.id == id).one()
        except BaseException:
            return None

    def count(self, cls=None):
        """Count the number of objects in storage"""
        return self.__session.query(cls).count()

    def close(self):
        """Call remove() method on the private session attribute"""
        self.__session.remove()
