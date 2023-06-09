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
        self.setGeometry(200, 200, 460, 480)
        self.setWindowOpacity(0.9) # Transparency setting max:1 min:0
        self.gui()

    def gui(self):

        self.lbl1 = QtWidgets.QLabel(self)
        guiName = "" # Type the program name
        self.lbl1.setText(guiName)
        self.lbl1.move(200,10)
        self.lbl1.setStyleSheet("background-color: #4180b3")

        self.info = QtWidgets.QPushButton(self)
        self.info.setText("?")
        self.info.setGeometry(400,10,57,30)
        self.info.setStyleSheet("background-color: #3498DB")

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

        self.lbl2 = QtWidgets.QLabel(self)
        self.lbl2.setText("Name*        :")
        self.lbl2.move(250,110)

        self.entry3 = QtWidgets.QLineEdit(self)
        self.entry3.move(320,110)
        
        self.lbl2 = QtWidgets.QLabel(self)
        self.lbl2.setText("Lastname* :")
        self.lbl2.move(250,150)

        self.entry3 = QtWidgets.QLineEdit(self)
        self.entry3.move(320,150)

        self.lbl2 = QtWidgets.QLabel(self)
        self.lbl2.setText("Username* :")
        self.lbl2.move(250,190)

        self.entry3 = QtWidgets.QLineEdit(self)
        self.entry3.move(320,190)

        self.lbl2 = QtWidgets.QLabel(self)
        self.lbl2.setText("Password* :")
        self.lbl2.move(250,230)

        self.entry3 = QtWidgets.QLineEdit(self)
        self.entry3.move(320,230)

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText("REGISTER")
        self.btn2.move(320,280)



def window():
    app = QApplication(sys.argv)
    window = mainForm()
    window.show()
    sys.exit(app.exec_())

window()