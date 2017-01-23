# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\pixiv下载器\main.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(290, 276)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        main.setFont(font)
        self.centralWidget = QtWidgets.QWidget(main)
        self.centralWidget.setObjectName("centralWidget")
        self.line = QtWidgets.QLineEdit(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(40, 60, 201, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(22)
        self.line.setFont(font)
        self.line.setText("")
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.b1 = QtWidgets.QPushButton(self.centralWidget)
        self.b1.setGeometry(QtCore.QRect(60, 130, 161, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.label2 = QtWidgets.QLabel(self.centralWidget)
        self.label2.setGeometry(QtCore.QRect(10, 245, 161, 21))
        self.label2.setText("")
        self.label2.setObjectName("label2")
        self.b2 = QtWidgets.QPushButton(self.centralWidget)
        self.b2.setGeometry(QtCore.QRect(30, 200, 75, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.b3 = QtWidgets.QPushButton(self.centralWidget)
        self.b3.setGeometry(QtCore.QRect(180, 200, 75, 23))
        self.b3.setObjectName("b3")
        main.setCentralWidget(self.centralWidget)

        self.retranslateUi(main)
        self.b3.clicked.connect(main.close)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "pixiv下载器"))
        self.label.setText(_translate("main", "输入ID号"))
        self.b1.setText(_translate("main", "下   载"))
        self.b2.setText(_translate("main", "登   陆"))
        self.b3.setText(_translate("main", "退  出"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())

