from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

# creating table for
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String, unique=True)
    city = Column(String)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime)

# Table card of users
class UserArticle(Base):
    __tablename__ = 'cards'
    article_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    article_number = Column(Integer, nullable=False)
    exp_date = Column(Integer, nullable=False)
    article_name = Column(String)





