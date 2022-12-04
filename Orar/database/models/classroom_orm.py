from sqlalchemy import Column, String, Integer

from database.base.sql_base import Base


class Classroom(Base):
    __tablename__ = 'classrooms'

    classroom_id = Column(Integer, primary_key=True)
    classroom_name = Column(String)

    def __init__(self, classroom_name):
        self.classroom_name = classroom_name

    def to_string(self):
        return f"{self.classroom_id} - {self.classroom_name}"

    def to_string_r(self):
        return f"{self.classroom_name}"
