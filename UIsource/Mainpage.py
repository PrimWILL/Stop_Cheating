from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class Main_Page(QWidget):
    switch_window_to_webcam = QtCore.pyqtSignal()
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(614, 436)

        self.label = QtWidgets.QLabel(MainForm)
        self.label.setGeometry(QtCore.QRect(30, 10, 211, 81))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("LoginInfo")

        self.label_2 = QtWidgets.QLabel(MainForm)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 91, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("SIDLabel")

        self.label_3 = QtWidgets.QLabel(MainForm)
        self.label_3.setGeometry(QtCore.QRect(60, 210, 71, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("NameLabel")

        self.WebcamTestButton = QtWidgets.QPushButton(MainForm)
        self.WebcamTestButton.setGeometry(QtCore.QRect(400, 70, 161, 101))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.WebcamTestButton.setFont(font)
        self.WebcamTestButton.setObjectName("WebcamTestButton")
        self.WebcamTestButton.clicked.connect(self.switch_webcam_page)

        self.TestStartButton = QtWidgets.QPushButton(MainForm)
        self.TestStartButton.setGeometry(QtCore.QRect(400, 230, 161, 101))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.TestStartButton.setFont(font)
        self.TestStartButton.setObjectName("TestStartButton")

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        #  그림 파일을 지정한다.
        MainForm.setWindowIcon(QIcon("UIsource/img-symbol.png"))
        MainForm.setWindowTitle(_translate("MainForm", "MainPage"))
        self.label.setText(_translate("MainForm", "로그인 정보"))
        self.label_2.setText(_translate("MainForm", "학번 : " ))
        self.label_3.setText(_translate("MainForm", "이름 : " ))
        self.WebcamTestButton.setText(_translate("MainForm", "웹캠 테스트"))
        self.TestStartButton.setText(_translate("MainForm", "시험 시작"))

    def switch_webcam_page(self):
        self.switch_window_to_webcam.emit()

