#!/usr/bin/python3
""" module for DB storage"""
import models
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import sqlalchemy
from os import getenv
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """defines database storage class """
    __engine = None
    __session = None
    all_classes = ["State", "City", "User", "Place", "Review"]

    def __init__(self):
        """initializer"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        exec_db = 'mysql+mysqldb://{}:{}@{}/{}'.format(
                                            HBNB_MYSQL_USER,
                                            HBNB_MYSQL_PWD,
                                            HBNB_MYSQL_HOST,
                                            HBNB_MYSQL_DB
                                                )
        self.__engine = create_engine(exec_db, pool_pre_ping=True)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ prints a query on current database session"""
        data = {}
        if cls is None:
            for curr in self.all_classes:
                curr = eval(curr)
                for instance in self.__session.query(curr).all():
                    key = instance.__class__.__name__ + '.' + instance.id
                    data[key] = instance
        else:
            for instance in self.__session.query(cls).all():
                key = instance.__class__.__name__ + '.' + instance.id
                data[key] = instance
        return data

    def new(self, obj):
        """creates new instance in db storage"""
        self.__session.add(obj)

    def save(self):
        """ save function"""
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes obj from db storage"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates database table"""
        Base.metadata.create_all(self.__engine)
        session_db = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_db)
        self.__session = Session()

    def close(self):
        """session ends"""
        self.reload()
        self.__session.close()
