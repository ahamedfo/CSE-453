from tkinter import CENTER
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PDFReader import PDFReader
import search



#file = "Amazon.pdf"
file_to_write = "order.csv"
outputt = []
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("dialog.ui", self)

        self.label = QLabel('This is label', self)
        self.label.setGeometry(QtCore.QRect(190, 250, 281, 31))
        self.label.setObjectName("label")
        #self.label.setText(_translate("MainWindow", "Output"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.label2 = QLabel('Line 1', self)
        self.label2.setGeometry(QtCore.QRect(140, 60, 281, 31))

        self.label3 = QLabel('Line 2', self)
        self.label3.setGeometry(QtCore.QRect(140, 115, 281, 31))

        self.label4 = QLabel('Line 3', self)
        self.label4.setGeometry(QtCore.QRect(140, 165, 281, 31))

        self.label5 = QLabel('Line 4', self)
        self.label5.setGeometry(QtCore.QRect(475, 60, 281, 31))

        self.label6 = QLabel('Line 5', self)
        self.label6.setGeometry(QtCore.QRect(475, 115, 281, 31))

        self.label6 = QLabel('Pet Name', self)
        self.label6.setGeometry(QtCore.QRect(475, 165, 281, 31))

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

        # Create textbox
        self.textbox6 = QLineEdit(self)
        self.textbox6.move(20, 20)
        self.textbox6.resize(280,40)
        self.textbox6.setGeometry(QtCore.QRect(340, 160, 131, 41))

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


        self.button = self.findChild(QPushButton, "pushButton")
        # connect button to function on_click
        self.button2.clicked.connect(self.on_enter)
        self.button1.clicked.connect(self.on_cancel)
        self.button.clicked.connect(self.on_openfile)
        self.button4.clicked.connect(self.on_correct_info)
        self.show()
        #self.label = self.findChild(QLabel, "label")

        
        self.show()

    def on_cancel(self):
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
        self.textbox5.setText("")
    def on_enter(self):
        dictt = { 'PetName':'0', 'Line1': '0', "Line2": '0', "Line3": '0', "Line4": '0', "Line5": '0'}
        textboxValue1 = self.textbox1.text()
        textboxValue2 = self.textbox2.text()
        textboxValue3 = self.textbox3.text()
        textboxValue4 = self.textbox4.text()
        textboxValue5 = self.textbox5.text()
        textboxValue6 = self.textbox6.text()

        if textboxValue1 != "":
            dictt["Line1"] = textboxValue1
        if textboxValue2 != "":
            dictt["Line2"] = textboxValue2
        if textboxValue3 != "":
            dictt["Line3"] = textboxValue3
        if textboxValue4 != "":
            dictt["Line4"] = textboxValue4
        if textboxValue5 != "":
            dictt["Line5"] = textboxValue5
        if textboxValue6 != "":
            dictt["PetName"] = textboxValue6
        
        output = textboxValue1 
        output += " "
        output += textboxValue2
        output += " "
        output += textboxValue3
        output += " "
        output += textboxValue4
        output += " "
        output += textboxValue5

        outputt = search.search(dictt, file_to_write)
        #search.right_entry = outputt
        self.label.setText(str(outputt))
        #self.label.setText(output)
        #QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        #self.textbox.setText("")

    def on_correct_info():
        search.right_entry = outputt


    def on_openfile(self):
        file = QFileDialog.getOpenFileName(self," Open File", "", "All Files (*);;Python Files (*.py)")
        outputfile = file[0].split("/")
        print(file)
        print(outputfile[len(outputfile) - 1])
        #reader = PDFReader(outputfile[len(outputfile) - 1],file_to_write)
        reader = PDFReader(file[0], file_to_write)
        reader.open_pdf()
        #processing.open_pdf(fd = outputfile[len(outputfile) - 1])
#initialize
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
