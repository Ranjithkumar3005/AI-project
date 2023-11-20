import sys
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from intial import Ui_Form

class mainfile(QDialog):
    def __init__(self):
        super(mainfile,self).__init__()
        self.firstUI=Ui_Form()
        self.firstUI.setupUi(self)
        
        self.firstUI.movie=QtGui.QMovie("D:\AI Project/Jarvis_Gui (2).gif")
        self.firstUI.label_2.setMovie(self.firstUI.movie)
        self.firstUI.movie.start()
        
        self.firstUI.pushButton.clicked.connect(self.connecttologin)
        self.firstUI.pushButton_2.clicked.connect(self.close)
        
    def connecttologin(self):
        from loginGUF import mainfile1
        self.showlogin=mainfile1()
        ui.close()
        self.showlogin.show()
        
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    ui=mainfile()
    ui.show()
    sys.exit(app.exec_())
    