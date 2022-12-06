from PyQt5.QtWidgets import QWidget, QTableWidget, QTableView


class GenerateWidget(QTableWidget):
    def __init__(self):
        QTableWidget.__init__(self, 2, 1)
        self.setFixedSize(300, 62)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setStretchLastSection(True)
        self.setSelectionBehavior(QTableView.SelectColumns)
        self.setSelectionMode(QTableView.SingleSelection)
        self.setDragDropMode(QTableWidget.DragDrop)
        self.setAcceptDrops(False)
