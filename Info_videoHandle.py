from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QStackedWidget, QMessageBox, QTabWidget
from Info_video import Ui_MainWindow
import sys


class InfoHandle(QMainWindow, Ui_MainWindow):
    def __init__(self, mainwindow=None):
        super().__init__()
        self.setupUi(mainwindow)
        
        