import json
import typing
from json import JSONEncoder

from PyQt5 import QtGui, QtCore, Qt
from PyQt5.QtCore import QByteArray, QMimeData
from PyQt5.QtGui import QDrag, QPixmap, QMouseEvent
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableView, QTableWidgetItem


class GenerateWidget(QTableWidget):

    def __init__(self):
        QTableWidget.__init__(self, 2, 1)
        self.teacher = None
        self.classroom = None
        self.subject = None
        self.setFixedSize(280, 62)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setStretchLastSection(True)
        self.setSelectionBehavior(QTableView.SelectColumns)
        self.setSelectionMode(QTableView.SingleSelection)
        self.setDragDropMode(QTableWidget.DragDrop)
        self.setAcceptDrops(False)
        self.setDragEnabled(True)

    def setMimeData(self):
        # data = json.dumps([self.model().index(0, 0), self.model().index(1, 1)])
        mime = QMimeData()
        arr = QByteArray()
        arr.append(json.dumps(self.teacher.to_dict()))
        arr.append(json.dumps(self.classroom.to_dict()))
        arr.append(json.dumps(self.subject.to_dict()))
        mime.setData("application/json", arr)
        return mime

    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        if e.buttons() == QtCore.Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mime = self.setMimeData()
            drag.setMimeData(mime)

            pixmap = QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)

            drag.exec_(QtCore.Qt.MoveAction)
