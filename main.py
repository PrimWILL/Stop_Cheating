from UIhandler import UIHandler
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


app = QtWidgets.QApplication(sys.argv)
uihandler = UIHandler()
uihandler.show_login_page()
sys.exit(app.exec_())



