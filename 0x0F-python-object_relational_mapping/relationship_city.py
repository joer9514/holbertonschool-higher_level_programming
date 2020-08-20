#!/usr/bin/python3
"""
Write a python file that contains the class definition
of a City and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from relationship_state import Base, State


class City(Base):
    """City Class"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
