#!/bin/usr/python3

"""
a script that define a state class and a base class
to work with MySqlAlchemy ORM
"""
from sqlalchemy import Column, String, Integer 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    A SQLAlchemy ORM model representing a state.

    Attributes:
        __tablename__(str): the name of the MySql table to store states. 
        id (int): The unique identifier for the state.
        name (str): The name of the state.
    """
    __tablename__ = "states"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(length= 128), nullable=False)
