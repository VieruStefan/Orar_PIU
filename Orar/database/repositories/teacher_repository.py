from database.base.sql_base import Session
from database.models.teacher_orm import Teacher


def get_teachers():
    session = Session()
    teachers = session.query(Teacher).all()
    return teachers


def get_teacher(teacher_id):
    session = Session()
    teacher = session.get(Teacher, teacher_id)
    return teacher


def add_teacher(first_name, last_name):
    session = Session()
    teacher = Teacher(first_name=first_name, last_name=last_name)
    try:
        session.add(teacher)
        session.commit()
    except Exception as exc:
        print(f"Failed to add teacher - {exc}")
    return teacher


def drop_teacher(teacher_id):
    session = Session()
    teacher = session.get(Teacher, teacher_id)
    try:
        session.delete(teacher)
        session.commit()
    except Exception as exc:
        print(f"Failed to delete teacher - {exc}")
    return teacher


def get_teacher_by_name(name):
    teachers = get_teachers()
    first_name = name.split()[0]
    last_name = name.split()[1]
    for teacher in teachers:
        if teacher.__getattribute__("first_name") == first_name\
                and teacher.__getattribute__("last_name") == last_name:
            return teacher
    return None
