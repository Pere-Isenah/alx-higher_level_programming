from sqlalchemy import Column, String, Integer 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = "states"
    id = Column(Integer,unique=True, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(length= 128),  nullable=False)
