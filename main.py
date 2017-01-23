# -*- coding: utf-8 -*-

import sys
import os
import requests
import PyQt5
import saveimg
import cookie
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

from Ui_main import Ui_main
import Ui_duihua

filename = 'cookie.txt'


class main(QMainWindow, Ui_main):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        self.setupUi(self)
        if os.path.exists(filename):
            self.label2.setText(u'已找到cookie')
        else:
            self.label2.setText(u'请登录')
        self.timer = QTimer(self) #初始化一个定时器
        self.timer.timeout.connect(self.operate) #计时结束调用operate()方法
        self.timer.start(500) #设置计时间隔并启动
    @pyqtSlot()
    def on_b1_clicked(self):
        self.b1.setDisabled(True)
        DictData={}
        if os.path.exists(filename):
            self.id = self.line.text()
            if self.id.isdigit():
                self.cookie=cookie.loadcookie(filename)
                DictData['id']=self.id
                DictData['cookie']=self.cookie
                self.Theading = Theading(DictData)
                self.Theading.sinout.connect(self.updateResult)
                self.Theading.start()  # 线程开始
            else:
                reply = QMessageBox.information(self,"消息",  "请输入正确ID", QMessageBox.Yes )
        else:
            reply = QMessageBox.information(self,"警告",  "没有cookie存在，请登录！", QMessageBox.Yes )
        self.b1.setDisabled(False)
    @pyqtSlot()
    def on_b2_clicked(self):

        dlg = Ui_duihua.dialog()
        dlg.exec_()

    def operate(self):
        if os.path.exists(filename):
            self.label2.setText(u'已找到cookie')
        else:
            self.label2.setText(u'请登录')
    @pyqtSlot()
    def updateResult(self,status):#结果处理
        if int(status)==4:
            reply = QMessageBox.information(self,"消息",  "没找到图片或者账号有问题，要不就是cookie失效或者官方改了接口。确认图片无误请清除下cookie试试", QMessageBox.Yes)
        else:
            reply = QMessageBox.information(self,"消息",  "应该成功了！", QMessageBox.Yes)

class Theading(QtCore.QThread):#新开线程
    sinout = pyqtSignal(str)
    def __init__(self, dict, parent=None):
        super(Theading, self).__init__(parent)
        self.dict = dict


    def run(self):
        result={}
        result['status'] =4
        self.id=self.dict['id']
        self.cookie=self.dict['cookie']
        self.yanzhen=saveimg.save(self.id,self.cookie)
        self.sinout.emit(str(self.yanzhen))


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    dlg = main()
    dlg.show()
    sys.exit(app.exec_())
#pyinstaller --hidden-import=queue --icon --paths E:/Python35/Lib/site-packages/PyQt5/Qt/bin -F  -w main.py