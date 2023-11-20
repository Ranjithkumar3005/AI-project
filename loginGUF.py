import sys
from PyQt5.QtWidgets import QWidget,QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import login
from login import Ui_Form
import faceGUF
import mainscreen_gif
from mainscreen_gif import Ui_MainWindow
class mainfile1(QWidget):
    def __init__(self):
        super(mainfile1,self).__init__()
        self.firstUI=Ui_Form()
        self.firstUI.setupUi(self)
        
        
        
        self.firstUI.lineEdit_2.setEchoMode(QLineEdit.Password)
        
        self.firstUI.movie=QtGui.QMovie("D:\AI Project/Earth.gif")
        self.firstUI.label_3.setMovie(self.firstUI.movie)
        self.firstUI.movie.start()
        
        self.firstUI.movie1=QtGui.QMovie("D:\AI Project/tenor.gif")
        self.firstUI.label_4.setMovie(self.firstUI.movie1)
        
        
        self.firstUI.pushButton.clicked.connect(self.facelogin)
        self.firstUI.pushButton_2.clicked.connect(self.validatelogin)
        self.firstUI.pushButton_3.clicked.connect(self.close)
        self.firstUI.pushButton_4.clicked.connect(self.retry)
        
        self.firstUI.label_4.hide()
        
    def facelogin(self):
        self.close()
        from faceGUF import mainfile2
        self.showface=mainfile2()
        self.showface.show()
      
      
    def validatelogin(self):
        username=self.firstUI.lineEdit.text()
        password=self.firstUI.lineEdit_2.text()
        
        if (username=="Ranjith" and password=="12345") or (username=="Magesh" and password=="12345") or (username=="Hemanth" and password=="12345") or (username=="Vithiya" and password=="12345") or (username=="Ezhil" and password=="12345"):
             print("Login success")
             from subprocess import call
             self.close()
             call(["python","mainscreen_gif.py"])
            
        else:
            self.logmovestart()
            
           
            
            
    def logmovestart(self):
        self.firstUI.label_4.show()
        self.firstUI.movie1.start()
        self.firstUI.lineEdit.hide()
        self.firstUI.lineEdit_2.hide()
        self.firstUI.label_6.hide()
        self.firstUI.label_7.hide()
        
    def logmovestop(self):
        self.firstUI.label_4.hide()
        self.firstUI.movie1.stop()
       
    def retry(self):
        self.firstUI.lineEdit.clear()
        self.firstUI.lineEdit_2.clear()
        self.logmovestop()
        self.firstUI.lineEdit.show()
        self.firstUI.lineEdit_2.show()
        self.firstUI.label_6.show()
        self.firstUI.label_7.show()
       
        
        
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    ui=mainfile1()
    ui.show()
    sys.exit(app.exec_())
    