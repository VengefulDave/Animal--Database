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
        self.RAlert.setText("")
        self.ReadMenuB.clicked.connect(self.gotoMenu)
        self.ReadEnterConfirm.clicked.connect(self.printid)

    def printid(self):
        readinput = self.ReadIdInput.text()

        if len(readinput)==0:
            self.RAlert.setText("Please Input In Animal Id")
        
        else:
            conn = sqlite3.connect("Actual Project/AnimalData.db")
            cursor = conn.cursor()
            selectanimal = cursor.execute("SELECT id, name, age, species, \
                                        breed, desexed, personality, \
                                        vaccination, injury, infections,\
                                        location, tbpd FROM data WHERE id = ?",(readinput,),).fetchall()
            if selectanimal == []:
                self.RAlert.setText("No Such Animal Id In Data Base")
            else:
                print(selectanimal)
                self.RAlert.setText("")
                self.RName.setText((selectanimal[0])[1])
                self.RAge.setText((selectanimal[0])[2])
                self.RSpecies.setText((selectanimal[0])[3])
                self.RBreed.setText((selectanimal[0])[4])
                self.RDesexed.setText((selectanimal[0])[5])
                self.RPerson.setText((selectanimal[0])[6])
                self.RVacc.setText((selectanimal[0])[7])
                self.RInjury.setText((selectanimal[0])[8])
                self.RInfect.setText((selectanimal[0])[9])
                self.RLocat.setText((selectanimal[0])[10])
                self.RTbpd.setText((selectanimal[0])[11])
                

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
        self.AAlert.setText("")
        self.AConfirmB.clicked.connect(self.AddId)
    
    def AddId(self):
        self.AAlert.setText("")
        addidinput = self.AddIdInput.text()
        addname = self.AName.text()
        addage = self.AAge.text()
        addspecies = self.ASpecies.text()
        addbreed = self.ABreed.text()
        adddesexed = self.ADesexed.text()
        addperson = self.APerson.text()
        addvacc = self.AVacc.text()
        addinjury = self.AInjury.text()
        addinfect = self.AInfect.text()
        addlocat = self.ALoc.text()
        addtbpd = self.ATbpd.text()
        
        conn = sqlite3.connect("Actual Project/AnimalData.db")
        cursor = conn.cursor()
        addcheck = cursor.execute("SELECT id FROM data WHERE id = ?",(addidinput,),).fetchall()
        
        if len(addidinput)== 0 or len(addname)== 0 or len(addage)== 0 or len(addspecies)== 0 or len(addbreed)== 0 \
            or len(adddesexed)== 0 or len(addperson)== 0 or len(addvacc)== 0 or len(addinjury)== 0 or len(addinfect)== 0 \
            or len(addlocat)== 0 or len(addtbpd) == 0:
            self.AAlert.setText("Please Fill In All Fields")

        else:
            try:
                (addcheck[0])[0] == addidinput
                self.AAlert.setText("Animal With Id '{}' Already Exists".format(addidinput))
            except:
                print("j")
            
    def gotoMenu(self):
        Menu = Menu_Ui()
        widget.addWidget(Menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
    


#Edit window class- Code for its interactable buttons.
class Edit_Ui(QDialog):
    def __init__(self):
        super(Edit_Ui, self).__init__()
        loadUi("Actual Project/EnterEditUi.ui",self)
        self.EditMenuB.clicked.connect(self.gotoMenu)
    
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

    