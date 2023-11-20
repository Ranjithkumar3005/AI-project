from fnmatch import translate
import sys
import time
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtCore import pyqtSlot,QTimer
import face_recognition
import cv2
import numpy 
import csv
import mainscreen_gif
import os
from datetime import datetime

from face import Ui_Form

class mainfile2(QWidget):
    def __init__(self):
        super(mainfile2,self).__init__()
        self.faceUI=Ui_Form()
        self.faceUI.setupUi(self)
        
        
        
        self.faceUI.movie=QtGui.QMovie("D:\AI Project/scanner.gif")
        self.faceUI.label_4.setMovie(self.faceUI.movie)
        self.faceUI.movie.start()
        
        
        self.name=None
        self.videoCapture_=None
        
        self.faceUI.label_8.clicked.connect(self.close)
        self.runProg()
    
    def runProg(self):
        self.videoCapture_ =0
        self.startVideo(self.videoCapture_)    
        
    @pyqtSlot()
    def startVideo(self,cameraName):
        print("Encoding started")
        if cameraName==1:
            self.capture=cv2.VideoCapture(int(cameraName))
        else:
            self.capture=cv2.VideoCapture(cameraName)
        self.timer=QTimer(self)
        path='images'
        if not os.path.exists(path):
            os.mkdir(path)
        
        images=[]
        self.classNames=[]
        self.encodeList=[]
        self.timeList1=[]
        self.timeList2=[]
        photolist=os.listdir(path)
        
        for cl in photolist:
            currentImage=cv2.imread(f'{path}/{cl}')
            images.append(currentImage)
            self.classNames.append(os.path.splitext(cl)[0])
            
        for img in images:
            
            boxes=face_recognition.face_locations(img)
            encodes_cur_frame=face_recognition.face_encodings(img,boxes)[0]
            self.encodeList.append(encodes_cur_frame)
            
        print("Faces encoded successfully")
        self.timer.timeout.connect(self.updateframes)
        self.timer.start(10)
    
    def updateframes(self):
        ret,self.image=self.capture.read()
        self.displayImage(self.image,self.encodeList,self.classNames,1)
        
    def displayImage(self,image,encodeList,className,window=1):
        image=cv2.resize(image,(391, 361))
        try:
            image=self.faceRec(image,encodeList,className)
            
        except Exception as e:
            print(e)
        qformat= QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformat= QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888
        outImage = QImage (image, image.shape[1], image.shape[0], image.strides[0], qformat)
        outImage = outImage.rgbSwapped()
        connect=False
        if window==1:
            self.faceUI.label_7.setPixmap(QPixmap.fromImage(outImage))
            self.faceUI.label_7.setScaledContents(True)
            if (self.name) is not None and self.name not in self.classNames:
                 _translate = QtCore.QCoreApplication.translate
                 self.faceUI.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:28pt; color:#ff0000;\">Face not match</span></p></body></html>"))
                  
            elif self.name  in self.classNames:
                 _translate = QtCore.QCoreApplication.translate
                 self.faceUI.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:28pt; color:#ff0000;\">Face matched</span></p></body></html>"))
                 self.faceUI.label_8.setEnabled(False)
                 self.faceUI.label_8.hide()
                 self.faceUI.label_9.setEnabled(True)
                 self.faceUI.label_9.show()
                 
                 self.faceUI.label_9.clicked.connect(self.connecttomain)
                 self.faceUI.label_9.clicked.connect(self.close)
                 cv2.waitKey(0)
                 cv2.destroyAllWindows()

                 

                
            
    def faceRec(self,image,encodeList,className):
        faces_cur_frame=face_recognition.face_locations(image)
        encodes_cur_frame=face_recognition.face_encodings(image,faces_cur_frame)
        
        for encodeFace,faceLoc in zip(encodes_cur_frame,faces_cur_frame):
            match=face_recognition.compare_faces(encodeList,encodeFace,tolerance=0.50)
            face_dis=face_recognition.face_distance(encodeList,encodeFace)
            self.name="Unknown"
            bestMatchIndex=numpy.argmin(face_dis)
            
            
            if match[bestMatchIndex]:
                self.name=className[bestMatchIndex]
                y1,x2,y2,x1=faceLoc
                cv2.rectangle(image,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.putText(image,self.name,(x1-6,y2+20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)
                
        return image
        
    def connecttomain(self):
        from subprocess import call
        self.close()
        self.capture.release()
        call(["python","mainscreen_gif.py"])
            
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    ui=mainfile2()
    ui.show()
    sys.exit(app.exec_())