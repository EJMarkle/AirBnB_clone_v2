#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os

class State(BaseModel, Base):
    """ State class """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete-orphan")

    else:
        name = ""

        @property
        def cities(self):
            """ cities getter """
            from models import storage
            city_list = []
            for city_id, city in storage.all("City").items():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
