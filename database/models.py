from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


# creating table for
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    city = Column(String)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime)


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)

    user_id = Column(Integer, ForeignKey('users.user_id'))

    post_name = Column(String)

    post_description = Column(String)

    exp_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')


