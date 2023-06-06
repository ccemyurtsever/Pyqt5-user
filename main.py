import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

from database import *


class mainForm(QMainWindow):
    def __init__(self):
        super(mainForm, self).__init__()
        self.setWindowIcon(QIcon("image/icon.png"))
        self.setWindowTitle("CCY - UserApp")
        self.setGeometry(200, 200, 500, 500)
        self.setWindowOpacity(0.9) # Transparency setting max:1 min:0
        self.gui()

    def gui(self):

        self.lbl1 = QtWidgets.QLabel(self)
        guiName = "" # Type the program name
        self.lbl1.setText(guiName)
        self.lbl1.move(200,10)
        self.lbl1.setStyleSheet("background-color: #4180b3")

        self.lbl2 = QtWidgets.QLabel(self)
        self.lbl2.setText("Username :")
        self.lbl2.move(25,110)

        self.lbl3 = QtWidgets.QLabel(self)
        self.lbl3.setText("Password :")
        self.lbl3.move(25,150)

        self.entry1 = QtWidgets.QLineEdit(self)
        self.entry1.move(85,110)

        self.entry2 = QtWidgets.QLineEdit(self)
        self.entry2.move(85,150)

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText("LOGIN")
        self.btn1.move(85,200)


def window():
    app = QApplication(sys.argv)
    window = mainForm()
    window.show()
    sys.exit(app.exec_())

    
window()