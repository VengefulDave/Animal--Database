#Importing SQL-(Database), PyQt5 and its Designer tool.
import sys
import typing
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtWidgets import QStackedWidget
import sqlite3


#Menu window class- Code for its interactable buttons.
class Menu_Ui(QDialog):
    def __init__(self):
        super(Menu_Ui, self).__init__()
        loadUi("Actual Project/MainUi.Ui", self)
        self.ReadB.clicked.connect(self.gotoRead)
        self.WriteB.clicked.connect(self.gotoAdd)
        self.EditB.clicked.connect(self.gotoEdit)                                                      
    
    def gotoRead(self):
        Read = Read_Ui()
        widget.addWidget(Read)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoAdd(self):
        Add = Add_Ui()
        widget.addWidget(Add)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotoEdit(self):
        Edit = Edit_Ui()
        widget.addWidget(Edit)
        widget.setCurrentIndex(widget.currentIndex()+1)

#Read window class- Code for its interactable buttons.
class Read_Ui(QDialog):
    def __init__(self):
        super(Read_Ui, self).__init__()
        loadUi("Actual Project/ReadUi.ui",self)
        self.ReadMenuB.clicked.connect(self.gotoMenu)
    
    def gotoMenu(self):
        Menu = Menu_Ui()
        widget.addWidget(Menu)
        widget.setCurrentIndex(widget.currentIndex()+1)

#Add window class- Code for its interactable buttons.
class Add_Ui(QDialog):
    def __init__(self):
        super(Add_Ui, self).__init__()
        loadUi("Actual Project/AddUi.ui",self)
        self.AddMenuB.clicked.connect(self.gotoMenu)
    
    def gotoMenu(self):
        Menu = Menu_Ui()
        widget.addWidget(Menu)
        widget.setCurrentIndex(widget.currentIndex()+1)

#Edit window class- Code for its interactable buttons.
class Edit_Ui(QDialog):
    def __init__(self):
        super(Edit_Ui, self).__init__()
        loadUi("Actual Project/EnterEditUi.ui",self)
        self.EditEnterMenu.clicked.connect(self.gotoMenu)
    
    def gotoMenu(self):
        Menu = Menu_Ui()
        widget.addWidget(Menu)
        widget.setCurrentIndex(widget.currentIndex()+1)


#Starts the program- Prompts Menu.
app = QApplication(sys.argv)
Menu=Menu_Ui()
widget = QStackedWidget()
widget.addWidget(Menu)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
#Exits any window when the top right button clicked.
try:
    sys.exit(app.exec_())
except:
    print("Exiting")