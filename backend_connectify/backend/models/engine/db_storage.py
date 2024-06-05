# backend_connectify/backend/models/engine/db_storage.py
#!/usr/bin/python3
"""
DBStorage Module
================

This module defines the DBStorage class, which provides an interface for
interacting with a MySQL database using SQLAlchemy. It supports basic
CRUD (Create, Read, Update, Delete) operations and handles database
sessions.

Classes:
--------
    DBStorage: A class to manage database storage for various models.

Usage:
------
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
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
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

classes = {"User": User, "Playlist": Playlist, "Track": Track, "Album": Album, "Chatroom": Chatroom, "Conversation": Conversation, "Session": Session}

class DBStorage:
    """Interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        
        """Instantiate a DBStorage object

        This initializes the database connection using environment
        variables for MySQL credentials and settings.
        """
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
        """Query all objects in the current database session

        Args:
            cls (str or class, optional): The class to query. If None,
                                          queries all classes.

        Returns:
            dict: A dictionary of all queried objects, keyed by
                  <class name>.<object id>.
        """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Add an object to the current database session

        Args:
            obj (BaseModel): The object to add to the session.
        """
        self.__session.add(obj)
        print("new user added from database storage")

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
        """Close the current session

        This method removes the current session, ensuring all changes are
        committed and the connection is closed properly.
        """
        self.__session.remove()
