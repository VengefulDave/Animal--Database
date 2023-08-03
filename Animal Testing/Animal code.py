import sys
import typing
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtWidgets import QStackedWidget
import sqlite3

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("Animal Testing/Animal Ui.ui", self)
        self.loginmain.clicked.connect(self.gotologin)
        self.signupb.clicked.connect(self.gotosignup)

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotosignup(self):
        signup = CreateAccScreen()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("Animal Testing/Animal Ui Login.ui",self)
        self.passf.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginlogin.clicked.connect(self.loginfunction)
    
    def loginfunction(self):
        user = self.userf.text()
        password = self.passf.text()

        if len(user)==0 or len(password)==0:
            self.alertlogin.setText("Please Input In All Fields")
        
        else:
            conn = sqlite3.connect("Animal Testing/Animal.db")
            cur = conn.cursor()
            query = 'SELECT pass FROM Animal WHERE user =\''+user+"\'"
            cur.execute(query)
            try:
                result_pass = cur.fetchone()[0]
                if result_pass == password:
                    print("Successfully logged in.")
                    self.alertlogin.setText("")

                else:
                    self.alertlogin.setText("Invalid username and/or password")
            except:
                self.alertlogin.setText("Invalid username and/or password")

class CreateAccScreen(QDialog):   
    def __init__(self):
        super(CreateAccScreen, self).__init__()
        loadUi("Animal Testing/signup.ui",self)
        self.passf.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passcf.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.signupfunction)
    
    def signupfunction(self):
        userf = self.userf.text()
        passf = self.passf.text()
        passcf = self.passcf.text()

        if len(userf)==0 or len(passf)==0 or len(passcf)==0:
            self.alertsign.setText("Please Input In All Fields")
        
        elif passf!= passcf:
            self.alertsign.setText("Passwords do not match")

        else: 
            conn = sqlite3.connect("Animal Testing/Animal.db")
            cur = conn.cursor()
            
            user_info = (userf, passf)
            cur.execute('INSERT INTO Animal (User, Pass) VALUES (?,?)', user_info)

            conn.commit()
            conn.close()

            print("Made An Account")
    

# main
app = QApplication(sys.argv)
welcome=WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(600)
widget.setFixedWidth(500)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")

