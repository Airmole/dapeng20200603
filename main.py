import random
import sys
import csv
import time
from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5 import QtCore, QtGui, QtWidgets
from ui import mainUI  #导入py文件中的类#ss是ui转换后的py文件，Ui_Form是文件中的类名




class win(QWidget,mainUI.Ui_Frame):  #继承类
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.setupUi(self)   #执行类中的setupUi函数



if __name__=='__main__':

    # 生成数据文件

    # 1. 创建文件对象
    f = open('data/data.csv', 'w+', encoding='utf-8')
    # 2. 基于文件对象构建 csv写入对象
    csv_writer = csv.writer(f)
    # 3. 构建列表头
    csv_writer.writerow(["rowID", "stamp", "datetime", "hum", "newhum", "co2"])
    # 4. 写入csv文件内容
    # csv_writer.writerow(["l", '18', '男'])
    for lines in range(2000):
        datetime = time.strftime("%Y-%m-%d %H:", time.localtime()) + str(int(lines/40)).zfill(2) + ":" + str(random.randint(10, 59))
        randHum = round(random.uniform(0.1, 99.9), 2)
        temp = round(100 - randHum, 2)
        co2 = round(random.uniform(5.1, 40.9), 2)
        csv_writer.writerow([lines, time.time(), datetime, randHum, temp, co2])
    # 5. 关闭文件
    f.close()

    app=QApplication(sys.argv)
    w=win()
    w.show()
    sys.exit(app.exec_())