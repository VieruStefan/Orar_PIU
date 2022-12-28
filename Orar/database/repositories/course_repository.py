from database.base.sql_base import Session

from database.repositories.classroom_repository import get_classroom_by_name
from database.repositories.teacher_repository import get_teacher_by_name
from database.repositories.subjects_repository import get_subject_by_acronym

from database.models.course_orm import Course


def get_courses():
    session = Session()
    courses = session.query(Course).all()
    return courses


def add_course(teacher_name, subject_acronym, classroom_name, course_length, course_type):
    session = Session()
    session.expire_on_commit = False
    teacher_id = get_teacher_by_name(teacher_name).teacher_id
    subject_id = get_subject_by_acronym(subject_acronym).subject_id
    classroom_id = get_classroom_by_name(classroom_name).classroom_id
    course = Course(teacher_id=teacher_id, subject_id=subject_id, classroom_id=classroom_id,
                    course_length=course_length, course_type=course_type)
    try:
        session.add(course)
        session.commit()
    except Exception as exc:
        print(f"Failed to add course - {exc}")
    return course

