# -*- coding:utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindows import MainWindow
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
#12