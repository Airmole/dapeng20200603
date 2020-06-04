# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'historyQueryUI.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!
import random

import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(696, 499)
        # Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textBrowser = QtWidgets.QTextBrowser(Frame)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 671, 481))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        strandArr = ["温度", "湿度", "二氧化碳浓度"]
        statusArr = ["正常", "过高", "过低", "略高", "略低", "适宜", "恰当", "清爽"]
        data = pd.read_csv("data/data.csv")
        list = data.values.tolist()
        contentStr = ""
        for line in range(len(list)):
            contentStr = contentStr + "<span>" + str(list[line][2]) + "     湿度：" + str(list[line][3]) + " 温度：" + str(list[line][4]) + " 二氧化碳浓度：" + str(list[line][5]) + "---------" + strandArr[random.randint(0, 2)] + "---------" + statusArr[random.randint(0, 7)] + "</span><br/>"



        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.textBrowser.setHtml(_translate("Frame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans CJK SC\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+ contentStr +"</p></body></html>"))

