import json

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QModelIndex, QEvent, QMetaType
from PyQt5.QtGui import QColor, QDropEvent, QEnterEvent
from PyQt5.QtWidgets import QTableWidget, QVBoxLayout, QTableWidgetItem, QAbstractItemView

from database.models.classroom_orm import Classroom
from database.models.subject_orm import Subject
from database.models.teacher_orm import Teacher
from database.repositories.classroom_repository import get_classroom, get_classroom_from_dict
from database.repositories.subjects_repository import get_subject, get_subject_from_dict
from database.repositories.teacher_repository import get_teacher_by_name, get_teacher, get_teacher_from_dict
from database.repositories.course_repository import add_course


class TableWidget(QTableWidget):

    def __init__(self, data, name):
        QTableWidget.__init__(self, 12, len(data))
        self.name = name
        self.data = data
        self.setData()
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setDragDropOverwriteMode(False)
        for i in range(len(self.data)): self.setColumnWidth(i, 80)

    def on_select(self, selected, deselected):

        for ix in selected.indexes():
            print('Selected Cell Location Row: {0}, Column: {1}'.format(ix.row(), ix.column()))

        for ix in deselected.indexes():
            print('Deselected Cell Location Row: {0}, Column: {1}'.format(ix.row(), ix.column()))

    def setData(self):
        horizontal_headers = []
        vertical_headers = []

        for n in self.data:
            horizontal_headers.append(n)
        self.setHorizontalHeaderLabels(horizontal_headers)

        for i in range(8, 20):
            vertical_headers.append(f"{i}")
        self.setVerticalHeaderLabels(vertical_headers)

        for row in range(self.rowCount()):
            for col in range(self.columnCount()):
                self.setItem(row, col, QTableWidgetItem())

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat("application/json"):
            e.acceptProposedAction()
        self.highlight(e.mimeData())

    def highlight(self, mime):
        [teacher, classroom, subject] = self.loadDataFromMime(mime)
        for row in range(self.rowCount()):
            for col in range(self.columnCount()):
                course_dict = self.item(row, col).whatsThis()
                if course_dict != "" and course_dict != "second row":
                    course_dict = json.loads(course_dict)
                    # if self.item(row, col).whatsThis() ==
                    if teacher.teacher_id == course_dict["teacher_id"] or \
                            classroom.classroom_id == course_dict["classroom_id"]:
                        for j in range(self.columnCount()):
                            self.item(row, j).setBackground(QColor(100, 0, 20))
                            self.item(row+1, j).setBackground(QColor(100, 0, 20))
        for row in range(self.rowCount()):
            for col in range(self.columnCount()):
                if self.item(row, col).background().color().getRgb() != QColor.fromRgb(100, 0, 20).getRgb()\
                        and self.item(row, col).text() == "":
                    self.item(row, col).setBackground(QColor(0, 100, 20))
                else:
                    self.item(row, col).setBackground(QColor(100, 0, 20))


    def dragLeaveEvent(self, e: QtGui.QDragLeaveEvent) -> None:
        for row in range(self.rowCount()):
            for col in range(self.columnCount()):
                self.item(row, col).setBackground(QColor(255, 255, 255))

    def dropEvent(self, e: QtGui.QDropEvent) -> None:
        index = self.indexAt(e.pos())
        if self.item(index.row(), index.column()).background() == QColor(0, 100, 20) and\
                self.item(index.row()+1, index.column()).background() == QColor(0, 100, 20):
            self.dropMimeData(e.mimeData(), e.dropAction(), index.row(), index.column())
        e.accept()
        for row in range(self.rowCount()):
            for col in range(self.columnCount()):
                self.item(row, col).setBackground(QColor(255, 255, 255))

    def dropMimeData(self, mime: QtCore.QMimeData, action: QtCore.Qt.DropAction, row: int, column: int):
        # setText - setam textul din textBox
        # setWhatsThis - setam un string de tipul:
        # {"first_name": "Robert", "teacher_id": 2, "last_name": "Lupu"}
        # {"classroom_name": "C2-6", "classroom_id": 2}
        # {"subject_id": 2, "subject_acronym": "PAOO", "subject_name": "Programarea aplicatiilor orientate obiect"}
        # pentru o celula pentru a sti ce date se afla in acele celule
        [teacher, classroom, subject] = self.loadDataFromMime(mime)
        course = add_course(teacher.to_string_r(),
                            subject.subject_acronym,
                            classroom.classroom_name, 2, "curs")

        self.item(row, column).setText(f"{subject.subject_acronym}")
        self.item(row + 1, column).setText(f"{teacher.last_name[0]}{teacher.first_name[0]} {classroom.classroom_name}")
        print(json.dumps(course.to_dict()))
        self.item(row, column).setWhatsThis(json.dumps(course.to_dict()))
        self.item(row + 1, column).setWhatsThis(f"second row")

    def loadDataFromMime(self, mime) -> [Teacher, Classroom, Subject]:
        arr = mime.data("application/json").data().decode("utf-8").replace("}", "}\n").split("\n")
        d = [json.loads(arr[0]), json.loads(arr[1]), json.loads(arr[2])]
        teacher = get_teacher_from_dict(d[0])
        classroom = get_classroom_from_dict(d[1])
        subject = get_subject_from_dict(d[2])
        return [teacher, classroom, subject]
