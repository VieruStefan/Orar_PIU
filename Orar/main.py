import sys
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QVBoxLayout, QWidget, QTabWidget
from interface.MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec())
