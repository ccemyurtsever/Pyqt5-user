import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

from database import *


class mainForm(QMainWindow):
    def __init__(self):
        super(mainForm, self).__init__()
        self.setWindowIcon(QIcon("icon.png"))
        self.setWindowTitle("CCY - UserApp")
        self.setGeometry(200, 200, 500, 500)
        self.setWindowOpacity(0.9)
        self.gui()

    def gui(self):
        self.lbl1 = QtWidgets.QLabel(self)
        guiName = "HERE" # Type the program name
        self.lbl1.setText(guiName)
        self.lbl1.move(200,10)
        self.lbl1.setStyleSheet("background-color: #4180b3")

def window():
    app = QApplication(sys.argv)
    window = mainForm()
    window.show()
    sys.exit(app.exec_())

    
window()