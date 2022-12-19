import json

from sqlalchemy import Column, String, Integer
from sqlalchemy_serializer import SerializerMixin

from database.base.sql_base import Base


class Teacher(Base, SerializerMixin):
    __tablename__ = 'teachers'

    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(192))
    last_name = Column(String(192))

    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name

    def to_string(self):
        return f"{self.teacher_id} - {self.first_name} - {self.last_name}"

    def to_string_r(self):
        return f"{self.first_name} {self.last_name}"
