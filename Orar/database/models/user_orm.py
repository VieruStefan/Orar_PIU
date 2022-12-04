from sqlalchemy import Column, String, Integer

from database.base.sql_base import Base


class User(Base):
    __tablename__ = 'users'

    username = Column(String, primary_key=True)
    password = Column(String)
    access_level = Column(Integer)

    def __init__(self, username, password, access_level):
        self.username = username
        self.password = password
        self.access_level = access_level
