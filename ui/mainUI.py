# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import dataMonitor
import historyQuery
import index
import lineStackMonitor
import setting


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(564, 386)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_5 = QtWidgets.QPushButton(Frame)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)
        # self.pushButton_6 = QtWidgets.QPushButton(Frame)
        # self.pushButton_6.setObjectName("pushButton_6")
        # self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(Frame)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton_5.setText(_translate("Frame", "历史查询"))
        self.pushButton_5.clicked.connect(self.openHistoryQuery)
        # self.pushButton_6.setText(_translate("Frame", "打印"))
        self.pushButton_4.setText(_translate("Frame", "设置"))
        self.pushButton_4.clicked.connect(self.openSetting)
        self.pushButton_2.setText(_translate("Frame", "监测数据"))
        self.pushButton_2.clicked.connect(self.openDataMonitor)
        self.pushButton_3.setText(_translate("Frame", "监测曲线"))
        self.pushButton_3.clicked.connect(self.openLineStackMonitor)
        self.pushButton.setText(_translate("Frame", "环境控制"))
        self.pushButton.clicked.connect(self.openEnvControl)

    def openEnvControl(self):
        self.envControlUI = index.win()
        self.envControlUI.show()

    def openDataMonitor(self):
        self.dataMonitorUI = dataMonitor.win()
        self.dataMonitorUI.show()

    def openLineStackMonitor(self):
        self.lineStackMonitorUI = lineStackMonitor.ChartView()
        self.lineStackMonitorUI.show()

    def openSetting(self):
        self.openSettingUI = setting.win()
        self.openSettingUI.show()

    def openHistoryQuery(self):
        self.openHistoryQueryUI = historyQuery.win()
        self.openHistoryQueryUI.show()
