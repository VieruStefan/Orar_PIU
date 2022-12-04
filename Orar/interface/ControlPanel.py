from PyQt5.QtWidgets import QVBoxLayout, QComboBox, QRadioButton, \
    QPushButton, QTextEdit, QWidget, QCalendarWidget, QScrollBar
from PyQt5.QtCore import Qt

from database.repositories.subjects_repository import get_subjects
from database.repositories.teacher_repository import get_teachers
from database.repositories.classroom_repository import get_classrooms


class ControlPanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(450, 500)
        self.vbox = QVBoxLayout()
        self.grupa = QTextEdit()
        self.materie = QComboBox()
        self.profesor = QComboBox()
        self.sala = QComboBox()
        self.curs = QRadioButton()
        self.laborator = QRadioButton()
        self.generare = QPushButton()
        self.calendar = QCalendarWidget()

        self.curs.setText("Curs")
        self.grupa.setFixedSize(100, 20)
        self.grupa.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.grupa.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.laborator.setText("Laborator")
        self.generare.setText("Generare")
        for teacher in get_teachers():
            self.profesor.addItem(f"{teacher.first_name} {teacher.last_name}")
        for classroom in get_classrooms():
            self.sala.addItem(f"{classroom.classroom_name}")
        for subject in get_subjects():
            self.materie.addItem(f"{subject.subject_name}")

        self.vbox.addWidget(self.grupa)
        self.vbox.addWidget(self.materie)
        self.vbox.addWidget(self.profesor)
        self.vbox.addWidget(self.sala)
        self.vbox.addWidget(self.curs)
        self.vbox.addWidget(self.laborator)
        self.vbox.addWidget(self.generare)
        self.vbox.addWidget(self.calendar)
        self.setLayout(self.vbox)

