import sys
from PyQt5.QtWidgets import QWidget,QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime

from face import Ui_Form

class mainfile2(QWidget):
    def __init__(self):
        super(mainfile2,self).__init__()
        self.faceUI=Ui_Form()
        self.faceUI.setupUi(self)
        
        video_capture = cv2.VideoCapture(0)
        jobs_image = face_recognition.load_image_file("pic_1.jpg")
        jobs_encoding = face_recognition.face_encodings(jobs_image)[0]

        ratan_tata_image = face_recognition.load_image_file("pic_2.jpg")
        ratan_tata_encoding = face_recognition.face_encodings(ratan_tata_image)[0]

        sadmona_image = face_recognition.load_image_file("pic_3.jpg")
        sadmona_encoding = face_recognition.face_encodings(sadmona_image)[0]

        tesla_image = face_recognition.load_image_file("pic_4.jpg")
        tesla_encoding = face_recognition.face_encodings(tesla_image)[0]

        known_face_encoding = [
             jobs_encoding,
             ratan_tata_encoding,
             sadmona_encoding,
             tesla_encoding
        ]

        known_faces_names = [
             "pic_1",
            "pic_2",
             "pic_3",
            "pic_4" 
        ]
        
        students = known_faces_names.copy()

        face_locations = []
        face_encodings = []
        face_names = []
        s=True

        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")

        f = open(current_date+'.csv','w+',newline = '')
        lnwriter = csv.writer(f)
        
        while True:
            _,self.faceUI.label_7 = video_capture.read()
            small_frame = cv2.resize(self.faceUI.label_7,(0,0),fx=0.25,fy=0.25)
            rgb_small_frame = small_frame[:,:,::-1]
            if s:
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings (rgb_small_frame, face_locations)
                face_names = []
                
                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
                    name=""
                    face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
                    best_match_index = np.argmin(face_distance)
                    if matches[best_match_index]:
                        name = known_faces_names[best_match_index]

                    face_names.append(name)
                    if name in known_faces_names:
                        if name in students:
                            students.remove(name)
                            print(students)
                            current_time = now.strftime("%H-%M-%S")
                            lnwriter.writerow([name,current_time])
            cv2.imshow("attendence system",self.faceUI.label_7)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()
        f.close()
                
        
        self.faceUI.label_8.clicked.connect(self.close)
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    ui=mainfile2()
    ui.show()
    sys.exit(app.exec_())