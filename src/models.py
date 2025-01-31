import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er



Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(80), nullable=False)
    password = Column(String(80), nullable=False)
    name = Column(String(250), nullable=False)
    email = Column(String(80), nullable=False)
    description = Column(String(250), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Post(Base):
    __tablename__ = 'post'

    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'),nullable=False)
    user = relationship(User)
    image = Column(String(250)nullable=False)
    description = Column(String(250), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    
class Comments(Base):
    __tablename__ = 'comments'

    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post = relationship(Post)
    content = Column(String(250), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Like(Base):
    __tablename__ = 'like'

    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post = relationship(Post)
    


class Follower(Base):
    __tablename__ = 'follower'

    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    follower = relationship(User)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    accepted = Column(Boolean())







    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
