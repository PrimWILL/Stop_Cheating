from PySide2.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Notice_Page(QWidget):
    switch_window_to_exam = QtCore.pyqtSignal()
    # counter 조절해서 N초 지정 가능
    counter = 10
    def setupUi(self, NoticeForm):
        NoticeForm.setObjectName("NoticeForm")
        NoticeForm.resize(614, 436)

        self.counter_label = QtWidgets.QLabel(NoticeForm)
        self.counter_label.setGeometry(QtCore.QRect(160, 250, 411, 221))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout_run)
        self.counter_label.setFont(font)
        self.counter_label.setObjectName("counter_label")


        self.notice_label = QtWidgets.QLabel(NoticeForm)
        self.notice_label.setGeometry(QtCore.QRect(50, 10, 541, 281))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.notice_label.setFont(font)
        self.notice_label.setObjectName("notice_label")

        self.retranslateUi(NoticeForm)
        QtCore.QMetaObject.connectSlotsByName(NoticeForm)

    def retranslateUi(self, NoticeForm):
        _translate = QtCore.QCoreApplication.translate
        NoticeForm.setWindowIcon(QIcon("UI/imgsource/img-symbol.png"))
        NoticeForm.setWindowTitle(_translate("NoticeForm", "NoticePage"))
        self.notice_label.setText(_translate("NoticeForm", "부정행위 감지 시 컴퓨터 화면과 캠 화면이 캡쳐됩니다.\n"
"          부정행위 감지 기준은 다음과 같습니다.\n"
"\n"
"\n"
"   1. 2명 이상의 사람이 캠 화면에 잡힌 경우\n"
"   2. 캠 화면에 휴대폰이 잡힌 경우\n"
"   3. 응시자가 자리를 비운 경우\n"
"   4. 답안지가 캠 화면에 잡히지 않는 경우"))

    def timeout_run(self):

        self.counter_label.setText(str(self.counter)+"초 후에 시험이 시작됩니다.")
        self.counter = self.counter -1
        if(self.counter == -1):
            self.switch_window_to_exam.emit()



