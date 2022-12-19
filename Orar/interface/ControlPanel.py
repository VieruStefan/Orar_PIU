from PyQt5.QtWidgets import QVBoxLayout, QComboBox, QRadioButton, \
    QPushButton, QTextEdit, QWidget, QCalendarWidget, QScrollBar, QTableWidgetItem
from PyQt5.QtCore import Qt

from database.models.course_orm import Course
from database.repositories.subjects_repository import get_subjects
from database.repositories.teacher_repository import get_teachers
from database.repositories.classroom_repository import get_classrooms
from interface.GenerateWidget import GenerateWidget


class ControlPanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.generated_course = None
        self.setFixedSize(300, 300)
        self.vbox = QVBoxLayout()
        self.materie = QComboBox()
        self.profesor = QComboBox()
        self.sala = QComboBox()
        self.curs = QRadioButton()
        self.laborator = QRadioButton()
        self.generare = QPushButton("Generare")
        self.generate_widget = GenerateWidget()

        self.curs.setText("Curs")
        self.laborator.setText("Laborator")

        for teacher in get_teachers():
            self.profesor.addItem(f"{teacher.first_name} {teacher.last_name}")
        for classroom in get_classrooms():
            self.sala.addItem(f"{classroom.classroom_name}")
        for subject in get_subjects():
            self.materie.addItem(f"{subject.subject_name}")

        self.vbox.addWidget(self.materie)
        self.vbox.addWidget(self.profesor)
        self.vbox.addWidget(self.sala)
        self.vbox.addWidget(self.curs)
        self.vbox.addWidget(self.laborator)
        self.vbox.addWidget(self.generare)
        self.vbox.addWidget(self.generate_widget)

        self.generare.clicked.connect(self.changelabeltext)
        self.setLayout(self.vbox)

    def changelabeltext(self):
        subject = None
        classroom = None
        teacher = None
        for materie in get_subjects():
            if f"{materie.subject_name}" == self.materie.currentText():
                subject = materie
                break

        for profesor in get_teachers():
            if f"{profesor.first_name} {profesor.last_name}" == self.profesor.currentText():
                teacher = profesor
                break

        for sala in get_classrooms():
            if f"{sala.classroom_name}" == self.sala.currentText():
                classroom = sala
                break

        self.generated_course = Course(subject_id=subject.subject_id,
                                       teacher_id=teacher.teacher_id,
                                       classroom_id=classroom.classroom_id,
                                       course_length=2,
                                       course_type=f"laborator")

        # aici se modifica tabelul de generat
        self.generate_widget.setItem(
            1, 0, QTableWidgetItem(f"{teacher.first_name[0]}{teacher.last_name[0]} {classroom.classroom_name}"))
        self.generate_widget.setItem(0, 0, QTableWidgetItem(subject.subject_acronym))
        self.generate_widget.teacher = teacher
        self.generate_widget.classroom = classroom
        self.generate_widget.subject = subject
        print(self.generated_course.to_string())
