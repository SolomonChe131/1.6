# -*- coding:utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
import wave as we
import pygame
import numpy as np
import struct
import scipy as sc
import math
import matplotlib.pyplot as plt
import os
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.Btn_sin.clicked.connect(self.signal_sine)
        self.Btn_ut.clicked.connect(self.signal_ut)
        self.Btn_rec.clicked.connect(self.signal_gt)
        self.Btn_ex.clicked.connect(self.signal_en)
    def signal_sine(self):
        x = np.linspace(0.1, 2 * np.pi, 41)
        y=np.sin(x)
        plt.stem(x,y)
        plt.show()
    def signal_ut(self):
        x=np.arange(-10,10,1)
        y=np.zeros(20)
        for index in range(len(x)):
            if(index>=10):
                y[index]=1
            else:
                y[index]=0
        plt.stem(x,y)
        plt.axis([-10,10,0,2])
        plt.show()
    def signal_gt(self):
        x=np.arange(-10,10,1)
        y=np.zeros(20)
        for index in range(len(x)):
            if(index>=5 and index<=15):
                y[index]=1
            else:
                y[index]=0
        plt.stem(x,y)
        plt.axis([-10,10,0,2])
        plt.show()
    def signal_en(self):
        x = np.linspace(0.1, 2 * np.pi, 41)
        y=np.exp(x)
        plt.stem(x,y)
        plt.show()
