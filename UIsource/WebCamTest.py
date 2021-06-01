import cv2
import sys
import numpy as np
from PySide2.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import qimage2ndarray



class Webcam_Page(QWidget):
    switch_window_to_main = QtCore.pyqtSignal()
    cap = cv2.VideoCapture(0)
    label = None
    timer = QTimer()

    def displayFrame(self):

        ret, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = qimage2ndarray.array2qimage(frame)
        self.label.setPixmap(QPixmap(image))
        self.label.setScaledContents(True)

    def start_timer(self):
        self.timer.timeout.connect(self.displayFrame)
        self.timer.start(60)

    def stop_timer(self):
        self.timer.stop()

    def setupUi(self, WebcamForm):
        WebcamForm.setObjectName("WebcamForm")
        WebcamForm.resize(614, 436)
        self.pushButton = QtWidgets.QPushButton(WebcamForm)
        self.pushButton.setGeometry(QtCore.QRect(320, 402, 281, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.switch_main_page)

        self.pushButton_2 = QtWidgets.QPushButton(WebcamForm)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 402, 281, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.start_timer)



        self.label = QtWidgets.QLabel(WebcamForm)
        self.label.setGeometry(QtCore.QRect(3, 1, 611, 381))
        self.label.setPixmap(QtGui.QPixmap("UIsource/cam.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(WebcamForm)
        QtCore.QMetaObject.connectSlotsByName(WebcamForm)

    def retranslateUi(self, WebcamForm):
        _translate = QtCore.QCoreApplication.translate
        WebcamForm.setWindowTitle(_translate("WebcamForm", "WebcamTest"))
        WebcamForm.setWindowIcon(QIcon("UIsource/img-symbol.png"))
        self.pushButton.setText(_translate("WebcamForm", "뒤로가기"))
        self.pushButton_2.setText(_translate("WebcamForm", "카메라 켜기"))

    def switch_main_page(self):
        self.switch_window_to_main.emit()




