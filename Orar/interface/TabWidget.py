from PyQt5.QtWidgets import QTabWidget


class TabWidget(QTabWidget):

    def __init__(self):
        QTabWidget.__init__(self)
        self.setFixedSize(1150, 415)

    def insert_tabs(self, list_tabs):
        for tab in list_tabs:
            self.addTab(tab, tab.name)
