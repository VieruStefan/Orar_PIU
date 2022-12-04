from PyQt5.QtWidgets import QVBoxLayout, QWidget,\
    QTabWidget, QHBoxLayout, QCalendarWidget

from interface.TableWidget import TableWidget
from interface.TabWidget import TabWidget
from interface.ControlPanel import ControlPanel

anul_1 = ['1106A', '1106B', '1107A', '1107B', '1108A', '1108B', '1109A', '1109B', '1110A', '1110B', '1111A', '1111B',
          '1112A', '1112B']
anul_2 = ['1206A', '1206B', '1207A', '1207B', '1208A', '1208B', '1209A', '1209B', '1210A', '1210B', '1211A', '1211B',
          '1212A', '1212B']
anul_3 = ['1306A', '1306B', '1307A', '1307B', '1308A', '1308B', '1309A', '1309B', '1310A', '1310B', '1311A', '1311B',
          '1312A', '1312B']
anul_4 = ['1406A', '1406B', '1407A', '1407B', '1408A', '1408B', '1409A', '1409B', '1410A', '1410B', '1411A', '1411B',
          '1412A', '1412B']


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 QTableView")
        self.setBaseSize(1400, 450)

        self.hbox = QHBoxLayout()
        self.table_1 = TableWidget(anul_1, "Anul 1")
        self.table_2 = TableWidget(anul_2, "Anul 2")
        self.table_3 = TableWidget(anul_3, "Anul 3")
        self.table_4 = TableWidget(anul_4, "Anul 4")
        self.tab_widget = TabWidget()
        self.control_panel = ControlPanel()

        self.tab_widget.insert_tabs([self.table_1, self.table_2, self.table_3, self.table_4])
        self.calendar = QCalendarWidget()

        self.hbox.addWidget(self.tab_widget)
        self.hbox.addWidget(self.control_panel)
        self.setLayout(self.hbox)
        self.show()

    def place_tab(self, table):
        tab = QWidget()
        vbox = QVBoxLayout()
        vbox.addWidget(table)
        tab.setLayout(vbox)
        self.tab_widget.addTab(tab, table.name)

