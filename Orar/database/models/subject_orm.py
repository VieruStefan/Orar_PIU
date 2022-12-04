from sqlalchemy import Column, String, Integer

from database.base.sql_base import Base


class Subject(Base):
    __tablename__ = 'subjects'

    subject_id = Column(Integer, primary_key=True)
    subject_acronym = Column(String)
    subject_name = Column(String)

    def __init__(self, subject_acronym, subject_name):
        self.subject_acronym = subject_acronym
        self.subject_name = subject_name

    def to_string(self):
        return f"{self.subject_id} - {self.subject_acronym} - {self.subject_name}"

    def to_string_r(self):
        return f"{self.subject_acronym} - {self.subject_name}"
