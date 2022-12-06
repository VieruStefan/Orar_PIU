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

        self.table_luni_anul_1 = TableWidget(anul_1, "Luni")
        self.table_luni_anul_2 = TableWidget(anul_2, "Luni")
        self.table_luni_anul_3 = TableWidget(anul_3, "Luni")
        self.table_luni_anul_4 = TableWidget(anul_4, "Luni")

        self.table_marti_anul_1 = TableWidget(anul_1, "Marti")
        self.table_marti_anul_2 = TableWidget(anul_2, "Marti")
        self.table_marti_anul_3 = TableWidget(anul_3, "Marti")
        self.table_marti_anul_4 = TableWidget(anul_4, "Marti")

        self.table_miercuri_anul_1 = TableWidget(anul_1, "Miercuri")
        self.table_miercuri_anul_2 = TableWidget(anul_2, "Miercuri")
        self.table_miercuri_anul_3 = TableWidget(anul_3, "Miercuri")
        self.table_miercuri_anul_4 = TableWidget(anul_4, "Miercuri")

        self.table_joi_anul_1 = TableWidget(anul_1, "Joi")
        self.table_joi_anul_2 = TableWidget(anul_2, "Joi")
        self.table_joi_anul_3 = TableWidget(anul_3, "Joi")
        self.table_joi_anul_4 = TableWidget(anul_4, "Joi")

        self.table_vineri_anul_1 = TableWidget(anul_1, "Vineri")
        self.table_vineri_anul_2 = TableWidget(anul_2, "Vineri")
        self.table_vineri_anul_3 = TableWidget(anul_3, "Vineri")
        self.table_vineri_anul_4 = TableWidget(anul_4, "Vineri")

        self.ani_tab = QTabWidget()
        self.anul_1_tab = TabWidget()
        self.anul_2_tab = TabWidget()
        self.anul_3_tab = TabWidget()
        self.anul_4_tab = TabWidget()

        self.anul_1_tab.insert_tabs([self.table_luni_anul_1, self.table_marti_anul_1,
                                     self.table_miercuri_anul_1, self.table_joi_anul_1,
                                     self.table_vineri_anul_1])

        self.anul_2_tab.insert_tabs([self.table_luni_anul_2, self.table_marti_anul_2,
                                     self.table_miercuri_anul_2, self.table_joi_anul_2,
                                     self.table_vineri_anul_2])

        self.anul_3_tab.insert_tabs([self.table_luni_anul_3, self.table_marti_anul_3,
                                     self.table_miercuri_anul_3, self.table_joi_anul_3,
                                     self.table_vineri_anul_3])

        self.anul_4_tab.insert_tabs([self.table_luni_anul_4, self.table_marti_anul_4,
                                     self.table_miercuri_anul_4, self.table_joi_anul_4,
                                     self.table_vineri_anul_4])

        self.ani_tab.addTab(self.anul_1_tab, "Anul 1")
        self.ani_tab.addTab(self.anul_2_tab, "Anul 2")
        self.ani_tab.addTab(self.anul_3_tab, "Anul 3")
        self.ani_tab.addTab(self.anul_4_tab, "Anul 4")

        self.control_panel = ControlPanel()

        self.hbox.addWidget(self.ani_tab)
        self.hbox.addWidget(self.control_panel)
        self.setLayout(self.hbox)
        self.show()

