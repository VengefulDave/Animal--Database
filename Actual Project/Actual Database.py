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
        self.EditB.clicked.connect(self.gotoEnterEdit)                                                      
    
    #Opens the read function GUI window.
    def gotoRead(self):
        Read = Read_Ui()
        widget.addWidget(Read)
        widget.setCurrentIndex(widget.currentIndex()+1)

    #Opens the add function GUI window.
    def gotoAdd(self):
        Add = Add_Ui()
        widget.addWidget(Add)
        widget.setCurrentIndex(widget.currentIndex()+1)

    #Opens the edit id checker function GUI window.
    def gotoEnterEdit(self):
        Edit = EnterEdit_Ui()
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
            #Looks for the animal id given inside the databse.
            conn = sqlite3.connect("Actual Project/AnimalData.db")
            cursor = conn.cursor()
            selectanimal = cursor.execute("SELECT id, name, age, species, \
                                        breed, desexed, personality, \
                                        vaccination, injury, infections,\
                                        location, tbpd FROM data WHERE id = ?",(readinput,),).fetchall()
            if selectanimal == []:
                self.RAlert.setText("No Such Animal Id In Data Base")
            else:
                #When and if it finds the id it writes the information down in the text bars.
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
                
    #Opens the menu window when menu button clicked.
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
        #Puts the information typed in boxes into variables.
        self.AAlert.setStyleSheet('font: 16pt "OCR A Extended"; color:red;')
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
        
        #Checks if the user missed any boxes.
        if len(addidinput)== 0 or len(addname)== 0 or len(addage)== 0 or len(addspecies)== 0 or len(addbreed)== 0 \
            or len(adddesexed)== 0 or len(addperson)== 0 or len(addvacc)== 0 or len(addinjury)== 0 or len(addinfect)== 0 \
            or len(addlocat)== 0 or len(addtbpd) == 0:
            self.AAlert.setText("Please Fill In All Fields")

        else:
            try:
                (addcheck[0])[0] == addidinput
                self.AAlert.setText("Animal With Id '{}' Already Exists".format(addidinput))
            except:
                #Puts all the inputed animal information into the database.
                conn = sqlite3.connect("Actual Project/AnimalData.db")
                cursor = conn.cursor()
                animalinfo = (addidinput, addname, addage, addspecies, addbreed, adddesexed, addperson, addvacc, addinjury, addinfect, addlocat, addtbpd)
                cursor.execute('INSERT INTO Data (Id, Name, Age, Species, Breed, Desexed, Personality, Vaccination, Injury,\
                                Infections, Location, TBPD) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', animalinfo)
                conn.commit()
                conn.close()
                self.AAlert.setStyleSheet('font: 16pt "OCR A Extended"; color:green;')
                self.AAlert.setText("Succesfully Added Animal Id/Information To DataBase!")

    #Opens the menu window when menu button clicked.
    def gotoMenu(self):
        Menu = Menu_Ui()
        widget.addWidget(Menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
    

#Edit window class- Code for its interactable buttons.
class Edit_Ui(QDialog):
    def __init__(self):
        super(Edit_Ui, self).__init__()
        loadUi("Actual Project/EditUi.ui",self)
        self.EditBackB.clicked.connect(self.gotoMenu)
        self.EAlert.setText("")
        self.EAlert.setStyleSheet('font: 16pt "OCR A Extended"; color:red;')
        self.EConfirmB.clicked.connect(self.saveanimal)
        
        #Writes all information about animal which id was given in EnterEdit GUI.
        EditChosenId2 = EditChosenId
        conn = sqlite3.connect("Actual Project/AnimalData.db")
        cursor = conn.cursor()
        selecteditanimal = cursor.execute("SELECT id, name, age, species, \
                                        breed, desexed, personality, \
                                        vaccination, injury, infections,\
                                        location, tbpd FROM data WHERE id = ?",(EditChosenId2,),).fetchall()
        print(selecteditanimal)
        self.EAlert.setText("")
        self.IdLabel.setText("  " + (selecteditanimal[0])[0])
        self.EName.setText((selecteditanimal[0])[1])
        self.EAge.setText((selecteditanimal[0])[2])
        self.ESpecies.setText((selecteditanimal[0])[3])
        self.EBreed.setText((selecteditanimal[0])[4])
        self.EDesexed.setText((selecteditanimal[0])[5])
        self.EPerson.setText((selecteditanimal[0])[6])
        self.EVacc.setText((selecteditanimal[0])[7])
        self.EInjury.setText((selecteditanimal[0])[8])
        self.EInfect.setText((selecteditanimal[0])[9])
        self.ELoc.setText((selecteditanimal[0])[10])
        self.ETbpd.setText((selecteditanimal[0])[11])

    def saveanimal(self):
        #Deletes old data that was attached to the given animal id.
        conn = sqlite3.connect("Actual Project/AnimalData.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM data WHERE id = '{}'".format(EditChosenId))

        addname = self.EName.text()
        addage = self.EAge.text()
        addspecies = self.ESpecies.text()
        addbreed = self.EBreed.text()
        adddesexed = self.EDesexed.text()
        addperson = self.EPerson.text()
        addvacc = self.EVacc.text()
        addinjury = self.EInjury.text()
        addinfect = self.EInfect.text()
        addlocat = self.ELoc.text()
        addtbpd = self.ETbpd.text()
        
        #Checks if the user missed any input boxes.
        if len(addname)== 0 or len(addage)== 0 or len(addspecies)== 0 or len(addbreed)== 0 \
            or len(adddesexed)== 0 or len(addperson)== 0 or len(addvacc)== 0 or \
            len(addinjury)== 0 or len(addinfect)== 0 \
            or len(addlocat)== 0 or len(addtbpd) == 0:
            self.EAlert.setStyleSheet('font: 16pt "OCR A Extended"; color:red;')
            self.EAlert.setText("Please Fill In All Fields")

        else:
            #Updates new information given into old given animal id.
            animalinfo = ( EditChosenId, addname, addage, addspecies, addbreed, adddesexed\
                      , addperson, addvacc, addinjury, addinfect, addlocat, addtbpd)
            cursor.execute('INSERT INTO Data (Id, Name, Age, Species, Breed, Desexed, Personality, Vaccination, Injury,\
                        Infections, Location, TBPD) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', animalinfo)
            conn.commit()
            conn.close()
            self.EAlert.setStyleSheet('font: 16pt "OCR A Extended"; color:green;')
            self.EAlert.setText("Succesfully Updated Animal Information!")

    #Opens the menu window when menu button clicked.
    def gotoMenu(self):
        Menu = Menu_Ui()
        widget.addWidget(Menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
    

#EnterEdit window class- Code for its interactable buttons.
class EnterEdit_Ui(QDialog):
    def __init__(self):
        super(EnterEdit_Ui, self).__init__()
        loadUi("Actual Project/EnterEditUi.ui",self)
        self.EditMenuB.clicked.connect(self.gotoMenu)
        self.EEConfirmB.clicked.connect(self.entereditMenu)
        self.EEAlert.setText("")

    def entereditMenu(self):
        #Looks for given animal id in database.
        choseneditid = self.EEIdInput.text()
        conn = sqlite3.connect("Actual Project/AnimalData.db")
        cursor = conn.cursor()
        selecteeanimal = cursor.execute("SELECT id FROM data WHERE id = ?",(choseneditid,),).fetchall()

        if len(choseneditid)==0:
            self.EEAlert.setText("Please Enter Animal Id Below")
        elif selecteeanimal== []:
            self.EEAlert.setText("No Such Animal Id In Data Base")
        else:
            #Opens the edit window with the chosen animal id.
            self.EEAlert.setText("")
            global EditChosenId
            EditChosenId = self.EEIdInput.text()
            Edit = Edit_Ui()
            widget.addWidget(Edit)
            widget.setCurrentIndex(widget.currentIndex()+1)
            
    #Opens the menu window when menu button clicked.
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

    