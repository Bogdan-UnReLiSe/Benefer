# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled_sw.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartServer(object):
    def setupUi(self, StartServer):
        StartServer.setObjectName("StartServer")
        StartServer.resize(499, 300)
        StartServer.setMinimumSize(QtCore.QSize(499, 300))
        StartServer.setMaximumSize(QtCore.QSize(1000, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Picture/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StartServer.setWindowIcon(icon)
        StartServer.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.gridLayout_2 = QtWidgets.QGridLayout(StartServer)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(StartServer)
        self.pushButton.setMinimumSize(QtCore.QSize(170, 48))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    font: 63 18pt \"Yu Gothic UI Semibold\";\n"
"    border-radius: 16px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.closeBut_2 = QtWidgets.QPushButton(StartServer)
        self.closeBut_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeBut_2.sizePolicy().hasHeightForWidth())
        self.closeBut_2.setSizePolicy(sizePolicy)
        self.closeBut_2.setMinimumSize(QtCore.QSize(48, 48))
        self.closeBut_2.setMaximumSize(QtCore.QSize(48, 48))
        self.closeBut_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeBut_2.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(76, 76, 76);\n"
"    border-radius: 12px\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(116, 116, 116);\n"
"    border-radius: 12px\n"
"}")
        self.closeBut_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Picture/svernut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeBut_2.setIcon(icon1)
        self.closeBut_2.setIconSize(QtCore.QSize(32, 32))
        self.closeBut_2.setCheckable(True)
        self.closeBut_2.setObjectName("closeBut_2")
        self.gridLayout_2.addWidget(self.closeBut_2, 0, 2, 1, 1)
        self.closeBut = QtWidgets.QPushButton(StartServer)
        self.closeBut.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeBut.sizePolicy().hasHeightForWidth())
        self.closeBut.setSizePolicy(sizePolicy)
        self.closeBut.setMinimumSize(QtCore.QSize(48, 48))
        self.closeBut.setMaximumSize(QtCore.QSize(48, 48))
        self.closeBut.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeBut.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(76, 76, 76);\n"
"    border-radius: 12px\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(116, 116, 116);\n"
"    border-radius: 12px\n"
"}")
        self.closeBut.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Picture/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeBut.setIcon(icon2)
        self.closeBut.setIconSize(QtCore.QSize(32, 32))
        self.closeBut.setCheckable(True)
        self.closeBut.setObjectName("closeBut")
        self.gridLayout_2.addWidget(self.closeBut, 0, 3, 1, 1)
        self.frame_2 = QtWidgets.QFrame(StartServer)
        self.frame_2.setMinimumSize(QtCore.QSize(481, 141))
        self.frame_2.setMaximumSize(QtCore.QSize(481, 141))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: \"Yu Gothic UI Semibold\";\n"
"border-top-right-radius: 16px;\n"
"border-top-left-radius: 16px;\n"
"font-size: 12pt;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.frame_2)
        self.plainTextEdit_2.setEnabled(False)
        self.plainTextEdit_2.setMinimumSize(QtCore.QSize(0, 0))
        self.plainTextEdit_2.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: \"Yu Gothic UI Semibold\";\n"
"text-align: center;")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout.addWidget(self.plainTextEdit_2, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 4)
        self.pushButton_5 = QtWidgets.QPushButton(StartServer)
        self.pushButton_5.setMinimumSize(QtCore.QSize(481, 58))
        self.pushButton_5.setMaximumSize(QtCore.QSize(481, 58))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    font: 63 12pt \"Yu Gothic UI Semibold\";\n"
"    border-bottom-right-radius: 16px;\n"
"    border-bottom-left-radius: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(175, 175, 175);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(215, 215, 215);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 2, 0, 1, 4)

        self.retranslateUi(StartServer)
        QtCore.QMetaObject.connectSlotsByName(StartServer)

    def retranslateUi(self, StartServer):
        _translate = QtCore.QCoreApplication.translate
        StartServer.setWindowTitle(_translate("StartServer", "StartServer"))
        self.pushButton.setText(_translate("StartServer", "Запуск сайта"))
        self.plainTextEdit_2.setPlainText(_translate("StartServer", "Запустите консоль, нажав на кнопку ниже, и впишите следующую команду:      ngrok http 5000\n"
"\n"
"После этого ваш сайт будет доступен по http-адресу, предоставленному в консоли."))
        self.pushButton_5.setText(_translate("StartServer", "Запустить консоль"))
