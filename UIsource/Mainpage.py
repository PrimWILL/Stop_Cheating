from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PySide2.QtCore import QTimer
import sys,datetime


class Main_Page(QWidget):
    switch_window_to_webcam = QtCore.pyqtSignal()
    switch_windows_to_exam = QtCore.pyqtSignal()

    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(614, 436)

        #label : label for Student info
        self.label = QtWidgets.QLabel(MainForm)
        self.label.setGeometry(QtCore.QRect(20, 30, 211, 81))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("LoginInfo")

        #label_2 : label for SID
        self.label_2 = QtWidgets.QLabel(MainForm)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 321, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("SIDLabel")

        #label_3 : label for name
        self.label_3 = QtWidgets.QLabel(MainForm)
        self.label_3.setGeometry(QtCore.QRect(60, 190, 321, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("NameLabel")

        #button for webcam test page
        self.WebcamTestButton = QtWidgets.QPushButton(MainForm)
        self.WebcamTestButton.setGeometry(QtCore.QRect(380, 90, 181, 111))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.WebcamTestButton.setFont(font)
        self.WebcamTestButton.setStyleSheet("background-color : rgb(55, 168, 255);\n"
                                            "color : rgb(0, 0, 0);\n"
                                            "border-radius : 15px;")
        self.WebcamTestButton.setObjectName("WebcamTestButton")
        self.WebcamTestButton.clicked.connect(self.switch_webcam_page)

        #test start button
        self.TestStartButton = QtWidgets.QPushButton(MainForm)
        self.TestStartButton.setGeometry(QtCore.QRect(380, 260, 181, 111))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.TestStartButton.setFont(font)
        self.TestStartButton.setStyleSheet("background-color : rgb(134, 255, 5);\n"
                                           "color : rgb(0, 0, 0);\n"
                                           "border-radius : 15px;")
        self.TestStartButton.setObjectName("TestStartButton")
        self.TestStartButton.clicked.connect(self.switch_exam_page)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

        #backgroundlabel : background(dynamic ajou)
        self.backgroundlabel = QtWidgets.QLabel(MainForm)
        self.backgroundlabel.setGeometry(QtCore.QRect(0, 0, 621, 441))
        self.backgroundlabel.setText("")
        self.backgroundlabel.setPixmap(QtGui.QPixmap("UIsource/imgsource/ajoumainpage.jpg"))
        self.backgroundlabel.setScaledContents(True)
        self.backgroundlabel.setObjectName("backgroundlabel")

        #label_4 : Current time label
        self.label_4 = QtWidgets.QLabel(MainForm)
        self.label_4.setGeometry(QtCore.QRect(310, 0, 301, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.timer = QTimer()
        self.timer.start(100)
        self.timer.timeout.connect(self.timeout_run)
        self.label_4.setObjectName("label_4")

        #this only appears when background is setted
        self.backgroundlabel.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.WebcamTestButton.raise_()
        self.TestStartButton.raise_()


    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowIcon(QIcon("UIsource/imgsource/img-symbol.png"))
        MainForm.setWindowTitle(_translate("MainForm", "MainPage"))
        self.label.setText(_translate("MainForm", "로그인 정보"))
        self.label_2.setText(_translate("MainForm", "학번 : " + self.SID))
        self.label_3.setText(_translate("MainForm", "이름 : " +self.Name))
        self.WebcamTestButton.setText(_translate("MainForm", "웹캠 테스트"))
        self.TestStartButton.setText(_translate("MainForm", "시험 시작"))

    #function for switching page
    def switch_webcam_page(self):
        self.switch_window_to_webcam.emit()

    def switch_exam_page(self):
        self.switch_windows_to_exam.emit()

    #function for updating current time for timer
    def timeout_run(self):
        current_time = datetime.datetime.now()
        self.label_4.setText(str(current_time.year)+"년 "+str(current_time.month)+"월 "+str(current_time.day)+"일 "+str(current_time.hour)+
                             "시 "+str(current_time.minute)+"분 "+str(current_time.second)+"초 ")

