from database.base.sql_base import Session
from database.models.classroom_orm import Classroom


def get_classrooms():
    session = Session()
    classrooms = session.query(Classroom).all()
    return classrooms


def get_classroom(classroom_id) -> Classroom:
    session = Session()
    classroom = session.get(Classroom, classroom_id)
    return classroom


def add_classroom(classroom_name):
    session = Session()
    classroom = Classroom(classroom_name=classroom_name)
    try:
        session.add(classroom)
        session.commit()
    except Exception as exc:
        print(f"Failed to add classroom - {exc}")
    return classroom


def drop_classroom(classroom_id):
    session = Session()
    classroom = session.get(Classroom, classroom_id)
    try:
        session.delete(classroom)
        session.commit()
    except Exception as exc:
        print(f"Failed to delete classroom - {exc}")
    return classroom


def get_classroom_by_name(classroom_name):
    classrooms = get_classrooms()
    for classroom in classrooms:
        if classroom.__getattribute__("classroom_name") == classroom_name:
            return classroom
    return None


def get_classroom_from_dict(d) -> Classroom:
    classroom = Classroom(d["classroom_name"])
    classroom.classroom_id = d["classroom_id"]
    return classroom
