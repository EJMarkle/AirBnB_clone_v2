#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from os import getenv
from datetime import datetime


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128),
                  nullable=False)
    state_id = Column(String(60),
                      ForeignKey('states.id'),
                      nullable=False)
    places = relationship("Place", backref="cities",
                          cascade="delete")

    def __init__(self, *args, **kwargs):
        """Instantiates a new City"""
        if 'updated_at' not in kwargs:
            kwargs['updated_at'] = datetime.utcnow()

        super().__init__(*args, **kwargs)
