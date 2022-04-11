from tkinter import CENTER
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import pdfplumber
import csv


endStatement = "the seller's name under the appropriate product. Then, in the \"Further Information\" section, click \"Contact the Seller.\""

headers = ['OrderNumber', 'FullName', "Address", "Pet Names", "SKU", "Color", "Line1",
           "line2", "line3", "line4", "line5"]

sep = " --- "
class CustomerOrder:
    def __init__(self, init_details, pet_name, sku, line1, line2, line3, line4, line5, color):
        self.finalOrder = []
        self.finalOrder.extend(init_details)
        self.finalOrder.append(sep.join(pet_name))
        self.finalOrder.append(sep.join(sku))
        self.finalOrder.append(sep.join(color))
        self.finalOrder.append(sep.join(line1))
        self.finalOrder.append(sep.join(line2))
        self.finalOrder.append(sep.join(line3))
        self.finalOrder.append(sep.join(line4))
        self.finalOrder.append(sep.join(line5))
        print(self.finalOrder)


class Track:

    def __init__(self, order_list):
        self.order_list = order_list
        self.pet_name = []
        self.order_items = []
        self.sku = []
        self.line1 = []
        self.line2 = []
        self.line3 = []
        self.line4 = []
        self.line5 = []
        self.color = []
        self.order_id = []

    def parse_each_order(self):
        for orders in self.order_list:
            sku = "SKU: "
            for order in range(len(orders)):
                if order == 0:
                    self.order_items.append(orders[order])
                elif sku in orders[order]:
                    self.sku.append(orders[order].split(" Tax")[0].split("SKU: ")[1])
                elif "Order Item ID:" in orders[order]:
                    self.order_id.append(orders[order].split("Order Item ID: ")[1])
                elif "Font Color:" in orders[order]:
                    self.color.append(orders[order].split("Font Color: ")[1].split(" (")[0])
                elif "Pet Name:" in orders[order]:
                    self.pet_name.append(orders[order].split("Pet Name: ")[1])
                elif "Line 1:" in orders[order]:
                    self.line1.append(orders[order].split("Line 1: ")[1])
                elif "Line 2:" in orders[order]:
                    self.line2.append(orders[order].split("Line 2: ")[1])
                elif "Line 3:" in orders[order]:
                    self.line3.append(orders[order].split("Line 3: ")[1])
                elif "Line 4:" in orders[order]:
                    self.line4.append(orders[order].split("Line 4: ")[1])
                elif "Line 5:" in orders[order]:
                    self.line5.append(orders[order].split("Line 5: ")[1])
                else:
                    continue

    def print_order(self):
        for i in self.order_list:
            print(i)

    def printAll(self):
        print(self.pet_name)
        print(self.sku)
        print(self.line1)
        print(self.line2)
        print(self.line3)
        print(self.line4)
        print(self.line5)
        print(self.color)
        print(self.order_id)


def open_pdf(fd):
    with pdfplumber.open(fd) as pdf:
        order = []
        # 12 14
        all_customers = []
        num = 0
        # 16,17
        for i in range(len(pdf.pages)):
            content = pdf.pages[i].extract_text().split('\n')
            num += 1
            if content[len(content) - 2] == endStatement:
                order.extend(content[1:-1])
                init_details = parse(order)
                total_order_list = find_total_order(order)
                order_details = subOrder(total_order_list)
                order_details.parse_each_order()
                # fill_with_Nonez()
                # order_details.printAll()

                customer = CustomerOrder(init_details, order_details.pet_name, order_details.sku, order_details.line1,
                                         order_details.line2,
                                         order_details.line3, order_details.line4, order_details.line5,
                                         order_details.color)
                all_customers.append(customer)
                order = []
            else:
                order.extend(content[1:-1])

    writeToCSV(all_customers)


def writeToCSV(customers):
    with open('order.csv', 'w', newline="", encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for i in customers:
            writer.writerow(i.finalOrder)
    f.close()


def find_total_order(array):
    total_order_list = []
    for i in range(0, len(array)):
        if "Grand total:" in array[i]:
            return total_order_list
        else:
            total_order_list.append(array[i])
    return total_order_list


def subOrder(array):
    order_list = []
    temp = []
    line = False
    for i in array:
        # case when there is another order
        if line and "Line " not in i:
            order_list.append(temp)
            line = False
            temp = [i]

        # Case for the first line
        elif not line and "Line " in i:
            line = True
            temp.append(i)
        else:
            temp.append(i)
    order_list.append(temp)
    # for i in order_list:
    #     print(i)
    return Track(order_list)


def parse(array):
    temp = []
    for i in array:
        if "Thank you" in i:
            break
        else:
            temp.append(i)

    name = temp[1].strip()
    fullAddess = "".join(temp[2:len(temp) - 2]).strip()
    order = temp[len(temp) - 1].split(' ')[2]

    return [order, name, fullAddess]

class UI(QMainWindow):
    
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("dialog.ui", self)

        self.label = QLabel('This is label', self)
        self.label.setGeometry(QtCore.QRect(190, 250, 281, 31))
        self.label.setObjectName("label")
        #self.label.setText(_translate("MainWindow", "Output"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)

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


        self.button = self.findChild(QPushButton, "pushButton")
        # connect button to function on_click
        self.button2.clicked.connect(self.on_enter)
        self.button1.clicked.connect(self.on_cancel)
        self.button.clicked.connect(self.on_openfile)
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
    def on_openfile(self):
        file = QFileDialog.getOpenFileName(self," Open File", "", "All Files (*);;Python Files (*.py)")
        outputfile = file[0].split("/")
        print(file)
        print(outputfile[len(outputfile) - 1])
        open_pdf(fd=outputfile)
#initialize
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
