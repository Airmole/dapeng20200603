import time
import random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import indexUI  #导入py文件中的类#ss是ui转换后的py文件，Ui_Form是文件中的类名

import sys

class win(QWidget,indexUI.Ui_Form):  #继承类
    def __init__(self):
        _translate = QtCore.QCoreApplication.translate
        strandArr = ["温度", "湿度", "二氧化碳浓度"]
        statusArr = ["正常", "过高", "过低", "略高", "略低", "适宜"]
        logStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "<h4>目前暂时一切正常，暂无报警。</h4><hr/>"
        for h in range(50):
            for i in range(len(strandArr)):
                logStr = logStr + "<span>" + time.strftime("%Y-%m-%d %H:%M", time.localtime()) + ":" + str(50-h) + " " + strandArr[i] + \
                         statusArr[random.randint(0, 5)] + "</span><br/>"
        else:
            print('log结束')




        super().__init__()
        self.resize(300, 300)
        self.setupUi(self, logStr)   #执行类中的setupUi函数



if __name__=='__main__':
    app=QApplication(sys.argv)
    w=win()
    w.show()
    sys.exit(app.exec_())