# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(544, 182)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Btn_sin = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_sin.setGeometry(QtCore.QRect(30, 110, 93, 28))
        self.Btn_sin.setObjectName("Btn_sin")
        self.Btn_ut = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_ut.setGeometry(QtCore.QRect(160, 110, 93, 28))
        self.Btn_ut.setObjectName("Btn_ut")
        self.Btn_rec = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_rec.setGeometry(QtCore.QRect(290, 110, 93, 28))
        self.Btn_rec.setObjectName("Btn_rec")
        self.Btn_ex = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_ex.setGeometry(QtCore.QRect(420, 110, 93, 28))
        self.Btn_ex.setObjectName("Btn_ex")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 20, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Btn_sin.setText(_translate("MainWindow", "sin[n]"))
        self.Btn_ut.setText(_translate("MainWindow", "u[n]"))
        self.Btn_rec.setText(_translate("MainWindow", "G[n]"))
        self.Btn_ex.setText(_translate("MainWindow", "e^[n]"))
        self.label.setText(_translate("MainWindow", "基本离散信号"))
