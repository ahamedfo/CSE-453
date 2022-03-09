from tkinter import CENTER
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        #self.setStyleSheet("background-color: blue;")
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 600
        self.initUI()
        
    def initUI(self):
        _translate = QtCore.QCoreApplication.translate
        self.label = QLabel('This is label', self)
        self.label.setGeometry(QtCore.QRect(190, 250, 281, 31))
        self.label.setObjectName("label")
        self.label.setText(_translate("MainWindow", "Output"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create textbox
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(20, 20)
        self.textbox1.resize(280,40)
        self.textbox1.setGeometry(QtCore.QRect(190, 60, 131, 41))
        

        # Create textbox
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(20, 20)
        self.textbox2.resize(280,40)
        self.textbox2.setGeometry(QtCore.QRect(190, 110, 131, 41))

        # Create textbox
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(20, 20)
        self.textbox3.resize(280,40)
        self.textbox3.setGeometry(QtCore.QRect(190, 160, 131, 41))

        # Create textbox
        self.textbox4 = QLineEdit(self)
        self.textbox4.move(20, 20)
        self.textbox4.resize(280,40)
        self.textbox4.setGeometry(QtCore.QRect(340, 60, 131, 41))

        # Create textbox
        self.textbox5 = QLineEdit(self)
        self.textbox5.move(20, 20)
        self.textbox5.resize(280,40)
        self.textbox5.setGeometry(QtCore.QRect(340, 110, 131, 41))

        # Create a button in the window
        self.button1 = QPushButton('Cancel', self)
        self.button1.move(20,80)
        self.button1.setGeometry(QtCore.QRect(200, 210, 113, 32))

        # Create a button in the window
        self.button2 = QPushButton('Enter', self)
        self.button2.move(20,80)
        self.button2.setGeometry(QtCore.QRect(350, 210, 113, 32))
        
        # Create a button in the window
        self.button3 = QPushButton('Incorrect Info', self)
        self.button3.move(20,80)
        self.button3.setGeometry(QtCore.QRect(200, 300, 113, 32))

        # Create a button in the window
        self.button4 = QPushButton('Correct Info', self)
        self.button4.move(20,80)
        self.button4.setGeometry(QtCore.QRect(350, 300, 113, 32))

        # connect button to function on_click
        self.button2.clicked.connect(self.on_enter)
        self.button1.clicked.connect(self.on_cancel)
        self.show()

        
    
    @pyqtSlot()
    def on_cancel(self):
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
        self.textbox5.setText("")
    def on_enter(self):
        textboxValue1 = self.textbox1.text()
        textboxValue2 = self.textbox2.text()
        textboxValue3 = self.textbox3.text()
        textboxValue4 = self.textbox4.text()
        textboxValue5 = self.textbox5.text()
        output = textboxValue1 
        output += " "
        output += textboxValue2
        output += " "
        output += textboxValue3
        output += " "
        output += textboxValue4
        output += " "
        output += textboxValue5
        self.label.setText(output)
        #QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        #self.textbox.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())