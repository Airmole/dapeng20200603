from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5 import QtCore, QtGui, QtWidgets
from ui import newSeetingUI  #导入py文件中的类#ss是ui转换后的py文件，Ui_Form是文件中的类名

import sys

class win(QWidget,newSeetingUI.Ui_Frame):  #继承类
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.setupUi(self)   #执行类中的setupUi函数



if __name__=='__main__':
    app=QApplication(sys.argv)
    w=win()
    w.show()
    sys.exit(app.exec_())