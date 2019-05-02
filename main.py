from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import core
import sys

print("Start application")
if __name__ == '__main__':
    app = QApplication([])              # lib
    app.setApplicationName("Crawler")   # lib
    game_core = core.Core()             # Create main game object
    sys.exit(app.exec_())               # running app
