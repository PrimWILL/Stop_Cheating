import cv2
import sys
import datetime
import numpy as np
from PySide2.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from kakaotalk.kakao import Kakaotalk
import qimage2ndarray

class Exam_Page(QWidget):
    switch_window_to_main = QtCore.pyqtSignal()
    VideoSignal = cv2.VideoCapture(0)
    timer = QTimer()
    count_person = 0
    count_time = 0

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
                    self.count_person += 1

                # bounding box와 confidence score 표시
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
                cv2.putText(frame, label + str(score), (x, y - 20), cv2.FONT_ITALIC, 0.5, (255, 255, 255), 1)

        # 사람 몇 명 찍히는지 console로 출력. 추후 삭제
        print(self.count_person)

        # 만약 이번 VideoCapture에서 사람이 2명 이상이라면, 시간에 추가
        if self.count_person > 1:
            self.count_time += 1
        self.count_person = 0

        # 만약 2명 이상 감지된 시간이 3초 이상이라면, capture
        # 근데 한 frame의 갱신 시간이 얼마인지 모르겠다... 여쭤보고 수정 필요
        if self.count_time > 50:
            self.save_picture()
            self.count_time = 0

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
        with open("coco.names", "r") as f:
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
        ExamForm.setWindowIcon(QIcon("UIsource/imgsource/img-symbol.png"))
        self.ExitButton.setText(_translate("ExamForm", "시험 종료"))

    # function for switching page
    def switch_main_page(self):
        self.stop_timer()
        self.VideoSignal.release()
        self.switch_window_to_main.emit()

    #function for save picture to folder ./images
    def save_picture(self):
        ret, img = self.VideoSignal.read()
        if ret:
            now = datetime.datetime.now()
            date = now.strftime('%Y%m%d')
            hour = now.strftime('%H%M%S')
            filename = './images/Test_{}_{}_{}_{}.png'.format(self.SID, self.Name, date, hour)
            cv2.imwrite(filename, img)

            # 카카오톡으로 부정행위가 의심되니 캡처된 사진을 확인해줄 것을 메세지로 전송
            kakao = Kakaotalk()
            kakao.send_message(self.SID, self.Name)

    # 키 입력 이벤트를 받아 사진 저장하는 임시 함수. 조건 구현 되면 CheatingDetected으로 이동
    def keyPressEvent(self, e):
        print(1)
        if e.key() == Qt.Key_Q:
            self.save_picture()





