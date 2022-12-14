from PyQt5.QtWidgets import QTableWidget, QVBoxLayout, QLabel, QWidget


class TableWidget(QTableWidget):

    def __init__(self, data, name):
        QTableWidget.__init__(self, 12, len(data))
        self.name = name
        self.data = data
        self.setData()
        self.setAcceptDrops(True)
        self.setDragEnabled(False)
        # self.setDragDropMode(QTableWidget.InternalMove)  # Objects can only be drag/dropped internally and are moved instead of copied
        # self.setDragDropOverwriteMode(False)
        for i in range(len(self.data)): self.setColumnWidth(i, 80)
        # self.selectionModel().selectionChanged.connect(self.on_data)

    def setData(self):
        horizontal_headers = []
        vertical_headers = []

        for n in self.data:
            horizontal_headers.append(n)
        self.setHorizontalHeaderLabels(horizontal_headers)

        for i in range(8, 20):
            vertical_headers.append(f"{i}")
        self.setVerticalHeaderLabels(vertical_headers)

    # def on_data(self):
    #     for item in self.selectedItems():
    #         item.setText("")


