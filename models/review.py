#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from models.base_model import Base
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base


class Review(BaseModel, Base):
    """ defines the Review class """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializer"""
        super().__init__(*args, **kwargs)
