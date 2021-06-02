import cv2

from UIsource.Loginpage import Login_Page
from UIsource.Mainpage import Main_Page
from UIsource.WebCamTest import Webcam_Page
from UIsource.Exampage import Exam_Page
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class UIHandler:
    def __init__(self):
        self.login_page = Login_Page()
        self.main_page = Main_Page()
        self.webcam_page = Webcam_Page()
        self.exam_page = Exam_Page()

        self.LoginForm = QtWidgets.QWidget()
        self.MainForm = QtWidgets.QWidget()
        self.WebcamForm = QtWidgets.QWidget()
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
        self.main_page.switch_windows_to_exam.connect(self.show_exam_page)
        self.MainForm.show()

    def show_webcam_page(self):
        self.MainForm.close()
        self.webcam_page.setupUi(self.WebcamForm)
        self.webcam_page.switch_window_to_main.connect(self.show_main_page)
        self.WebcamForm.show()

    def show_exam_page(self):
        self.exam_page.SID = self.login_page.SID
        self.exam_page.Name = self.login_page.Name
        self.MainForm.close()
        self.exam_page.setupUi(self.ExamForm)
        self.exam_page.switch_window_to_main.connect(self.show_main_page)
        self.ExamForm.show()