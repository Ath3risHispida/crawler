from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainMenu:

    def __init__(self):
        print("Start Main Menu")
        self.Window = QWidget()
        self.Window.setFixedSize(500, 500)
        self.Window.setWindowTitle("Crawler")
        self.Window.show()