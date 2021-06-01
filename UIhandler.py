import cv2

from UIsource.Loginpage import Login_Page
from UIsource.Mainpage import Main_Page
from UIsource.WebCamTest import Webcam_Page
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class UIHandler:
    def __init__(self):
        self.login_page = Login_Page()
        self.main_page = Main_Page()
        self.webcam_page = Webcam_Page()

        self.LoginForm = QtWidgets.QWidget()
        self.MainForm = QtWidgets.QWidget()
        self.WebcamForm = QtWidgets.QWidget()

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
        self.main_page.setupUi(self.MainForm)
        self.main_page.switch_window_to_webcam.connect(self.show_webcam_page)
        self.MainForm.show()

    def show_webcam_page(self):
        self.MainForm.close()
        self.webcam_page.setupUi(self.WebcamForm)
        self.webcam_page.switch_window_to_main.connect(self.show_main_page)
        self.WebcamForm.show()