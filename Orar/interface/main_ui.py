from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from TableWidget import TableWidget


class Window(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1478, 854)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layout = QVBoxLayout()

        self.table = TableWidget()
        self.table.width = 200
        self.table.height = 1200
        self.layout.addWidget(self.table)

        self.centralwidget.setLayout(self.layout)
