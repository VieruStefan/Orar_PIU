from sqlalchemy import Column, String, Integer, Table, ForeignKey

from base.sql_base import metadata_obj, engine

from database.repositories.teacher_repository \
    import get_teachers, add_teacher, drop_teacher, get_teacher, get_teacher_by_name
from database.repositories.subjects_repository \
    import get_subjects, add_subject, drop_subject, get_subject, get_subject_by_acronym
from database.repositories.classroom_repository \
    import get_classrooms, add_classroom, drop_classroom, get_classroom, get_classroom_by_name
from database.repositories.course_repository \
    import add_course, get_courses


def recreate():
    teachers = Table(
        "teachers",
        metadata_obj,
        Column("teacher_id", Integer, primary_key=True, autoincrement=True),
        Column("first_name", String(192)),
        Column("last_name", String(192))
    )
    subjects = Table(
        "subjects",
        metadata_obj,
        Column("subject_id", Integer, primary_key=True, autoincrement=True),
        Column("subject_acronym", String(192)),
        Column("subject_name", String(192))
    )
    classrooms = Table(
        "classrooms",
        metadata_obj,
        Column("classroom_id", Integer, autoincrement=True, primary_key=True),
        Column("classroom_name", String(192))
    )
    courses = Table(
        "courses",
        metadata_obj,
        Column("subject_id", Integer, ForeignKey("subjects.subject_id"), primary_key=True),
        Column("teacher_id", Integer, ForeignKey("teachers.teacher_id")),
        Column("classroom_id", Integer, ForeignKey("classrooms.classroom_id")),
        Column("course_length", Integer),
        Column("course_type", String(192))
    )

    metadata_obj.drop_all(engine)
    metadata_obj.create_all(engine)


if __name__ == '__main__':
    recreate()
    add_teacher("Marius", "Gavrilescu")
    add_teacher("Robert", "Lupu")
    add_teacher("Alexandru", "Archip")
    add_teacher("Tiberius", "Dumitriu")
    add_subject("PIU", "Proiectarea interfetelor pentru utilizator")
    add_subject("PAOO", "Programarea aplicatiilor orientate obiect")
    add_subject("POS", "Programare orientata pe servicii")
    add_subject("EP", "Evaluarea performantelor")
    add_classroom("AC-03")
    add_classroom("C0-3")
    add_classroom("C2-6")
    add_classroom("C2-7")

    print(f"\nTeachers:")
    for teacher in get_teachers():
        print(teacher.to_string(), end="\n")

    print(f"\nSubjects:")
    for subject in get_subjects():
        print(subject.to_string(), end="\n")

    print(f"\nClassrooms:")
    for classroom in get_classrooms():
        print(classroom.to_string(), end="\n")

    print(f"\nCourses:")
    for course in get_courses():
        print(course.to_string(), end="\n")

    # print(get_subject_by_acronym("PIU"))
    # print(get_teacher_by_name("Robert Lupu"))
    # print(get_teacher_by_name("Robert Lupuu"))
    # print(get_classroom_by_name("AC-03"))
    # print(get_classroom_by_name("C0-3"))
