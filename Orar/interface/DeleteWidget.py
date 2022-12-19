from PyQt5.QtWidgets import QPushButton, QTableWidget



class DeleteWidget(QPushButton):

    def __init__(self):
        QPushButton.__init__(self)
        self.setFixedSize(30, 260)
        self.setStyleSheet('QPushButton {font-size: 20px;}')
        self.setText('D\nE\nL\nE\nT\nE\n')




