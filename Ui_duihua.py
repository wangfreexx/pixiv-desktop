# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\pixiv下载器\duihua.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

import cookie
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(321, 321)
        dialog.setSizeGripEnabled(True)
        self.line1 = QtWidgets.QLineEdit(dialog)
        self.line1.setGeometry(QtCore.QRect(30, 60, 251, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.line1.setFont(font)
        self.line1.setText("")
        self.line1.setObjectName("line1")
        self.line2 = QtWidgets.QLineEdit(dialog)
        self.line2.setGeometry(QtCore.QRect(30, 140, 251, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.line2.setFont(font)
        self.line2.setText("")
        self.line2.setObjectName("line2")
        self.line2.setEchoMode(QLineEdit.Password)
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 91, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 91, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 200, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 290, 141, 31))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 270, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "登陆"))
        self.label.setText(_translate("dialog", "账  号"))
        self.label_2.setText(_translate("dialog", "密  码"))
        self.pushButton.setText(_translate("dialog", "登  陆"))
        self.pushButton_2.setText(_translate("dialog", "清除cookie"))

class dialog(QDialog, Ui_dialog):
    def __init__(self, parent=None):
        super(dialog, self).__init__(parent)
        self.setupUi(self)
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.pid = self.line1.text()
        self.password = self.line2.text()
        if self.pid=='' or  self.password=='':
            reply = QMessageBox.information(self,"消息",  "请输入账号和密码！", QMessageBox.Yes)
        else:
            self.yanzhen=cookie.getcookies(pid=self.pid, password=self.password)
            if self.yanzhen==4:
                reply = QMessageBox.information(self,"消息",  "出错，请重试（并不是账号密码错误）！", QMessageBox.Yes )
            else:
                reply = QMessageBox.information(self,"消息",  "保存cookie成功，注意仅仅是保存成功，密码不对不一定能用！", QMessageBox.Yes)
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        filename = 'cookie.txt'
        if os.path.exists(filename):
            os.remove(filename)
            reply = QMessageBox.information(self,"消息",  "清除成功", QMessageBox.Yes)
        else:
             reply = QMessageBox.information(self,"消息",  "没了！", QMessageBox.Yes)

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    dlg = dialog()
    dlg.show()
    sys.exit(app.exec_())

