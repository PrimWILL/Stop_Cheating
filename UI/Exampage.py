from PySide2.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from kakaotalk.kakao import Kakaotalk
from PIL import ImageGrab
import cv2
import os
import sys
import datetime
import numpy as np
import qimage2ndarray

class Exam_Page(QWidget):
    switch_window_to_main = QtCore.pyqtSignal()
    show_alert_page_1 = QtCore.pyqtSignal()
    show_alert_page_2 = QtCore.pyqtSignal()
    show_alert_page_3 = QtCore.pyqtSignal()
    show_alert_page_4 = QtCore.pyqtSignal()
    VideoSignal = cv2.VideoCapture(0)
    timer = QTimer()
    count_person1 = 0
    count_cellphone = 0
    count_paper = 0
    count_time_alert1 = 0
    count_time_alert2 = 0
    count_time_alert3 = 0
    count_time_alert4 = 0

    def displayFrame(self):
        ret, frame = self.VideoSignal.read()
        h, w, c = frame.shape

        #웹캠에서 프레임 입력받아 전처리
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        self.YOLO_net.setInput(blob)
        outs = self.YOLO_net.forward(self.output_layers)

        class_ids = []
        confidences = []
        boxes = []

        for out in outs:

            for detection in out:

                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                # 검출 신뢰도
                if confidence > 0.1:
                    # Object detected
                    # 검출기의 경계상자 좌표는 0 ~ 1로 정규화되어있으므로 다시 전처리
                    center_x = int(detection[0] * w)
                    center_y = int(detection[1] * h)
                    dw = int(detection[2] * w)
                    dh = int(detection[3] * h)
                    # Rectangle coordinate
                    x = int(center_x - dw / 2)
                    y = int(center_y - dh / 2)
                    boxes.append([x, y, dw, dh])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.45, 0.4)

        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(self.classes[class_ids[i]])
                score = confidences[i]

                # 만약에 label이 person이라면, person 수에 추가
                if label == 'person':
                    self.count_person1 += 1
                if label == 'cell phone':
                    self.count_cellphone +=1
                if label == 'paper':
                    self.count_paper +=1



                # bounding box와 confidence score 표시
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
                cv2.putText(frame, label + str(score), (x, y - 20), cv2.FONT_ITALIC, 0.5, (255, 255, 255), 1)
        #alert3 : no person
        if(self.count_person1 == 0):
            self.count_time_alert3 +=1
            print("alert3 count : no person" + str(self.count_time_alert3))
        #alert4 = no paper
        if(self.count_paper == 0):
            self.count_time_alert4 +=1
            print("alert4 count : no paper" + str(self.count_time_alert4))

        # alert1 : more than 1 person
        if self.count_person1 > 1:
            self.count_time_alert1 += 1
            print("alert1 count : more than 1 person" + str(self.count_time_alert1))
        self.count_person1 = 0

        if self.count_time_alert1 > 10:
            self.save_picture()
            self.show_alert_page_1.emit()
            self.count_time_alert1 = 0

        # alert2 : cellphone
        if self.count_cellphone > 0:
            self.count_time_alert2 += 1
            print("alert2 count : cellphone" + str(self.count_time_alert2))
        self.count_cellphone = 0

        if self.count_time_alert2 > 10:
            self.save_picture()
            self.show_alert_page_2.emit()
            self.count_time_alert2 = 0

        #alert3 : no person
        if self.count_time_alert3 > 10:
            self.save_picture()
            self.show_alert_page_3.emit()
            self.count_time_alert3=0

        #alert4 : no paper
        if self.count_time_alert4 > 5:
            self.save_picture()
            self.show_alert_page_4.emit()
            self.count_time_alert4=0




        #Pyqt Label에 bounding box포함해 전처리한 프레임 입력
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = qimage2ndarray.array2qimage(frame)
        self.YoloLabel.setPixmap(QPixmap(image))
        self.YoloLabel.setScaledContents(True)

    #라벨 프레임 갱신을 위한 타이머(60ms마다 갱신) (성능향상에 영향x)
    def start_timer(self):
        self.timer.timeout.connect(self.displayFrame)
        self.timer.start(60)

    def stop_timer(self):
        self.timer.stop()

    def setupUi(self, ExamForm):
        ExamForm.setObjectName("ExamForm")
        ExamForm.resize(614, 436)

        #Yolo framework
        self.YOLO_net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
        self.classes = []
        with open("cheating.names", "r") as f:
            self.classes = [line.strip() for line in f.readlines()]
        self.layer_names = self.YOLO_net.getLayerNames()
        self.output_layers = [self.layer_names[i[0] - 1] for i in self.YOLO_net.getUnconnectedOutLayers()]

        self.YoloLabel = QtWidgets.QLabel(ExamForm)
        self.YoloLabel.setGeometry(QtCore.QRect(0, 0, 621, 441))
        self.YoloLabel.setObjectName("YoloLabel")
        self.start_timer()

        #click button to return main page
        self.ExitButton = QtWidgets.QPushButton(ExamForm)
        self.ExitButton.setGeometry(QtCore.QRect(420, 380, 181, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.ExitButton.setFont(font)
        self.ExitButton.setStyleSheet("background-color : rgb(39, 136, 255);\n"
"color : rgb(255, 255, 255);\n"
"border-radius : 15px;")
        self.ExitButton.setObjectName("ExitButton")
        self.ExitButton.clicked.connect(self.switch_main_page)



        self.retranslateUi(ExamForm)
        QtCore.QMetaObject.connectSlotsByName(ExamForm)

        # this only appears when background is setted
        self.YoloLabel.raise_()
        self.ExitButton.raise_()

    def retranslateUi(self, ExamForm):
        _translate = QtCore.QCoreApplication.translate
        ExamForm.setWindowTitle(_translate("ExamForm", "ExamPage"))
        ExamForm.setWindowIcon(QIcon("UI/imgsource/img-symbol.png"))
        self.ExitButton.setText(_translate("ExamForm", "시험 종료"))

    # function for switching page
    def switch_main_page(self):
        self.stop_timer()
        self.VideoSignal.release()
        self.switch_window_to_main.emit()

    #function for save picture to folder ./images
    #웹캠 화면과 컴퓨터 화면 스크린샷 찍어서 ./images폴더에 저장
    def save_picture(self):
        ret, img = self.VideoSignal.read()
        if ret:
            now = datetime.datetime.now()
            date = now.strftime('%Y%m%d')
            hour = now.strftime('%H%M%S')
            # 웹캠 화면 캡쳐
            filename = './images/Webcam_{}_{}_{}_{}.png'.format(self.SID, self.Name, date, hour)

            self.ko2Uni_save(filename, img)
            # self.imwrite(filename, img)

            # 컴퓨터 화면스크린 샷도 찍어서 저장
            Screen_filename = './images/Screenshot_{}_{}_{}_{}.png'.format(self.SID, self.Name, date, hour)
            screen_img=ImageGrab.grab()
            screen_img.save(Screen_filename)

            # 카카오톡으로 부정행위가 의심되니 캡처된 사진을 확인해줄 것을 메세지로 전송
            #kakao = Kakaotalk()
            #kakao.send_message(self.SID, self.Name, date, hour)

    def ko2Uni_save(self, filename, img):
        extension = os.path.splitext(filename)[1]
        result, n = cv2.imencode(extension, img, None)
        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)




