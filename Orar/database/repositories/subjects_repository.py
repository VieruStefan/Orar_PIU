from database.base.sql_base import Session
from database.models.subject_orm import Subject


def get_subjects():
    session = Session()
    subjects = session.query(Subject).all()
    return subjects


def get_subject(subject_id):
    session = Session()
    subject = session.get(Subject, subject_id)
    return subject


def add_subject(subject_acronym, subject_name):
    session = Session()
    subject = Subject(subject_acronym=subject_acronym, subject_name=subject_name)
    try:
        session.add(subject)
        session.commit()
    except Exception as exc:
        print(f"Failed to add subject - {exc}")
    return subject


def drop_subject(subject_id):
    session = Session()
    subject = session.get(Subject, subject_id)
    try:
        session.delete(subject)
        session.commit()
    except Exception as exc:
        print(f"Failed to delete subject - {exc}")
    return subject


def get_subject_by_acronym(subject_acronym):
    subjects = get_subjects()
    for subject in subjects:
        if subject.__getattribute__("subject_acronym") == subject_acronym:
            return subject
    return None
