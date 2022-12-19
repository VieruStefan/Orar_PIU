import json

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QModelIndex, QEvent, QMetaType
from PyQt5.QtGui import QColor, QDropEvent, QEnterEvent
from PyQt5.QtWidgets import QTableWidget, QVBoxLayout, QTableWidgetItem, QAbstractItemView

from database.repositories.classroom_repository import get_classroom
from database.repositories.subjects_repository import get_subject
from database.repositories.teacher_repository import get_teacher_by_name, get_teacher


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
            print("gee")
        for row in range(self.rowCount()):
            for col in range(self.columnCount()):
                if self.item(row, col).text() == "":
                    self.item(row, col).setBackground(QColor(0, 100, 20))
                else:
                    self.item(row, col).setBackground(QColor(100, 0, 20))

    def dragLeaveEvent(self, e: QtGui.QDragLeaveEvent) -> None:
        for row in range(self.rowCount()):
            for col in range(self.columnCount()):
                self.item(row, col).setBackground(QColor(255, 255, 255))

    def dropEvent(self, e: QtGui.QDropEvent) -> None:
        index = self.indexAt(e.pos())
        parent = index.parent()
        self.dropMimeData(e.mimeData(), e.dropAction(), index.row(), index.column())
        e.accept()
        for row in range(self.rowCount()):
            for col in range(self.columnCount()):
                self.item(row, col).setBackground(QColor(255, 255, 255))

    def dropMimeData(self, mime: QtCore.QMimeData, action: QtCore.Qt.DropAction, row: int, column: int):
        str = mime.data("application/json").data().decode("utf-8")
        str = str.replace("}", "}\n")
        print(str)
        arr = str.split("\n")


        d = [json.loads(arr[0]), json.loads(arr[1]), json.loads(arr[2])]
        teacher_id = d[0]["teacher_id"]
        classroom_id = d[1]["classroom_id"]
        subject_id = d[2]["subject_id"]

        teacher = get_teacher(f"{teacher_id}")
        classroom = get_classroom(f"{classroom_id}")
        subject = get_subject(f"{subject_id}")

        self.item(row, column).setData(0, arr)
        self.item(row, column).setText(f"{subject.subject_acronym}")
        self.item(row+1, column).setText(f"{teacher.first_name[0]}{teacher.last_name[0]} {classroom.classroom_name}")