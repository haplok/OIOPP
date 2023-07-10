# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Password.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(215, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(215, 200))
        MainWindow.setMaximumSize(QtCore.QSize(215, 200))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_Password = QtWidgets.QLabel(self.centralwidget)
        self.label_Password.setObjectName("label_Password")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_Password)
        self.lineEdit_Password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Password)
        self.pushButton_Enter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Enter.setObjectName("pushButton_Enter")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton_Enter)
        self.pushButton_Back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton_Back)
        self.textEdit_Changelog = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Changelog.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.textEdit_Changelog.setObjectName("textEdit_Changelog")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.textEdit_Changelog)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_Enter.clicked.connect(self.lineEdit_Password.copy)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_Password.setText(_translate("MainWindow", "Введите пароль"))
        self.pushButton_Enter.setText(_translate("MainWindow", "Войти"))
        self.pushButton_Back.setText(_translate("MainWindow", "Я не знаю пароль"))
