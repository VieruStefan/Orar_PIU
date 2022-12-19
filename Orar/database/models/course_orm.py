from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy_serializer import SerializerMixin

from database.base.sql_base import Base
from database.repositories.subjects_repository import get_subject
from database.repositories.teacher_repository import get_teacher
from database.repositories.classroom_repository import get_classroom


class Course(Base, SerializerMixin):
    __tablename__ = 'courses'

    subject_id = Column(Integer, ForeignKey("subjects.subject_id"), primary_key=True)
    teacher_id = Column(Integer, ForeignKey("teachers.teacher_id"))
    classroom_id = Column(Integer, ForeignKey("classrooms.classroom_id"))
    course_length = Column(Integer)
    course_type = Column(String)

    def __init__(self, subject_id, teacher_id, classroom_id, course_length, course_type):
        self.course_length = course_length
        self.course_type = course_type
        self.subject_id = subject_id
        self.teacher_id = teacher_id
        self.classroom_id = classroom_id

    def to_string(self):
        subject = get_subject(self.subject_id)
        teacher = get_teacher(self.teacher_id)
        classroom = get_classroom(self.classroom_id)
        return f"{subject.to_string_r()} - {teacher.to_string_r()} - {classroom.to_string_r()} - {self.course_type} - {self.course_length} ore"
