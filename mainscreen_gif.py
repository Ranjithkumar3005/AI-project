import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import  *
from PyQt5.QtGui import *



import os
import cv2
from mainscreen import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class MainThread(QThread):
    def _init_(self):
        super(MainThread, self)._init_()
        
    def run(self) -> None:
        return super().run()

startExec = MainThread()
class mainScreenGIF(QMainWindow):
    def __init__(self,window):
        super(mainScreenGIF,self).__init__()
        print("Setting Up GUI")

        self.firstUI = Ui_MainWindow()
        self.firstUI.setupUi(window)
        
        self.firstUI.End_button.clicked.connect(self.close)

        #GIF
        self.firstUI.movie = QtGui.QMovie("./Iron_Template_1.gif")
        self.firstUI.bg_gif1.setMovie(self.firstUI.movie)
        self.firstUI.movie.start()
        
        self.firstUI.movie = QtGui.QMovie("./live.gif")
        self.firstUI.bg_gif2.setMovie(self.firstUI.movie)
        self.firstUI.movie.start()
        
        self.firstUI.movie = QtGui.QMovie("./Earth.gif")
        self.firstUI.bg_gif3.setMovie(self.firstUI.movie)
        self.firstUI.movie.start()
        
        
        self.firstUI.movie = QtGui.QMovie("./__1.gif")
        self.firstUI.circle_gif.setMovie(self.firstUI.movie)
        self.firstUI.movie.start()
        
        # timer = QTimer(self)
        # timer.timeout.connect(self.showTimeLive)
        # timer.start(999)
        # startExec.start()
        
        # def showTimeLive():
        #     t_ime = QTime.currentTime()
        #     time = t_ime.toString()
        #     d_ate = QDate.currentDate()
        #     date =d_ate.toString()
        #     label_time = "Time : "+time
        #     label_date = "Date : "+date
            
        #     self.firstUI.Time_lab1.setText(label_time)
        #     self.firstUI.Time_lab2.setText(label_date)
        #timer = QTimer(self)
 
        # adding action to timer
#        timer.timeout.connect(self.showTime)
 
        # update the timer every second
 #       timer.start(1000)
 
    # method called by timer
    #def showTime(self):
 
        # getting current time
     #   current_time = QTime.currentTime()
 
        # converting QTime object to string
      #  label_time = current_time.toString('hh:mm:ss')
 
        #d_ate = QDate.currentDate()
       # date =d_ate.toString()
        # showing it to the label
        ##self.firstUI.Time_lab1.setText(label_time)
        #self.firstUI.Time_lab2.setText(date)

            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = mainScreenGIF(window=MainWindow)
    MainWindow.show()
    
    # ui = mainScreenGIF()
    # ui.show()
    exit(app.exec_())