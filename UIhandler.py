from UI.Loginpage import Login_Page
from UI.Mainpage import Main_Page
from UI.WebCamTest import Webcam_Page
from UI.Noticepage import Notice_Page
from UI.Exampage import Exam_Page
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import sys
import cv2


class UIHandler:
    def __init__(self):
        self.login_page = Login_Page()
        self.main_page = Main_Page()
        self.webcam_page = Webcam_Page()
        self.notice_page = Notice_Page()
        self.exam_page = Exam_Page()

        self.LoginForm = QtWidgets.QWidget()
        self.MainForm = QtWidgets.QWidget()
        self.WebcamForm = QtWidgets.QWidget()
        self.NoticeForm = QtWidgets.QWidget()
        self.ExamForm = QtWidgets.QWidget()

    def show_login_page(self):
        self.MainForm.close()
        self.login_page.setupUi(self.LoginForm)
        self.login_page.switch_window_to_main.connect(self.show_main_page)
        self.LoginForm.show()

    def show_main_page(self):
        self.main_page.SID = self.login_page.SID
        self.main_page.Name = self.login_page.Name
        self.LoginForm.close()
        self.WebcamForm.close()
        self.ExamForm.close()
        self.main_page.setupUi(self.MainForm)
        self.main_page.switch_window_to_webcam.connect(self.show_webcam_page)
        self.main_page.switch_window_to_notice.connect(self.show_notice_page)
        self.MainForm.show()

    def show_webcam_page(self):
        self.MainForm.close()
        self.webcam_page.setupUi(self.WebcamForm)
        self.webcam_page.switch_window_to_main.connect(self.show_main_page)
        self.WebcamForm.show()

    def show_notice_page(self):
        self.MainForm.close()
        self.notice_page.setupUi(self.NoticeForm)
        self.notice_page.switch_window_to_exam.connect(self.show_exam_page)
        self.NoticeForm.show()

    def show_exam_page(self):
        self.exam_page.SID = self.login_page.SID
        self.exam_page.Name = self.login_page.Name
        self.NoticeForm.close()
        self.exam_page.setupUi(self.ExamForm)
        self.exam_page.switch_window_to_main.connect(self.show_main_page)
        self.exam_page.show_alert_page_1.connect(self.show_alert_page1)
        self.exam_page.show_alert_page_2.connect(self.show_alert_page2)
        self.exam_page.show_alert_page_3.connect(self.show_alert_page3)
        self.exam_page.show_alert_page_4.connect(self.show_alert_page4)
        self.ExamForm.show()

    def show_alert_page1(self):
        alert1 = QMessageBox()
        alert1.setIcon(QMessageBox.Warning)
        alert1.setText("부정행위가 감지되었습니다.")
        alert1.setWindowTitle("ALERT")
        alert1.setInformativeText('사유 : 사람이 2명 이상 감지되었습니다.')
        alert1.exec_()

    def show_alert_page2(self):
        alert2 = QMessageBox()
        alert2.setIcon(QMessageBox.Warning)
        alert2.setText("부정행위가 감지되었습니다.")
        alert2.setWindowTitle("ALERT")
        alert2.setInformativeText('사유 : 휴대폰이 검출되었습니다.')
        alert2.exec_()

    def show_alert_page3(self):
        alert3 = QMessageBox()
        alert3.setIcon(QMessageBox.Warning)
        alert3.setText("부정행위가 감지되었습니다.")
        alert3.setWindowTitle("ALERT")
        alert3.setInformativeText('사유 : 응시자가 자리를 이탈했습니다.')
        alert3.exec_()

    def show_alert_page4(self):
        alert4 = QMessageBox()
        alert4.setIcon(QMessageBox.Warning)
        alert4.setText("부정행위가 감지되었습니다.")
        alert4.setWindowTitle("ALERT")
        alert4.setInformativeText('사유 : 시험지,답안지가 화면에 잡히지 않습니다.')
        alert4.exec_()
