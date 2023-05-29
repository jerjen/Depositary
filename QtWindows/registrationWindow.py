# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registrationWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_registrationWindow(object):
    def setupUi(self, registrationWindow):
        registrationWindow.setObjectName("registrationWindow")
        registrationWindow.resize(900, 700)
        self.startLabel = QtWidgets.QLabel(registrationWindow)
        self.startLabel.setGeometry(QtCore.QRect(0, 0, 901, 100))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.startLabel.setFont(font)
        self.startLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.startLabel.setAutoFillBackground(False)
        self.startLabel.setStyleSheet("")
        self.startLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.startLabel.setWordWrap(False)
        self.startLabel.setObjectName("startLabel")
        self.lastNameLabel = QtWidgets.QLabel(registrationWindow)
        self.lastNameLabel.setGeometry(QtCore.QRect(240, 100, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lastNameLabel.setFont(font)
        self.lastNameLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lastNameLabel.setAutoFillBackground(False)
        self.lastNameLabel.setStyleSheet("")
        self.lastNameLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lastNameLabel.setWordWrap(False)
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.firstNameLabel = QtWidgets.QLabel(registrationWindow)
        self.firstNameLabel.setGeometry(QtCore.QRect(240, 220, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.firstNameLabel.setFont(font)
        self.firstNameLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.firstNameLabel.setAutoFillBackground(False)
        self.firstNameLabel.setStyleSheet("")
        self.firstNameLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.firstNameLabel.setWordWrap(False)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.loginLabel = QtWidgets.QLabel(registrationWindow)
        self.loginLabel.setGeometry(QtCore.QRect(240, 340, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.loginLabel.setFont(font)
        self.loginLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.loginLabel.setAutoFillBackground(False)
        self.loginLabel.setStyleSheet("")
        self.loginLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.loginLabel.setWordWrap(False)
        self.loginLabel.setObjectName("loginLabel")
        self.passLabel = QtWidgets.QLabel(registrationWindow)
        self.passLabel.setGeometry(QtCore.QRect(240, 450, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.passLabel.setFont(font)
        self.passLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.passLabel.setAutoFillBackground(False)
        self.passLabel.setStyleSheet("")
        self.passLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.passLabel.setWordWrap(False)
        self.passLabel.setObjectName("passLabel")
        self.lastNameLineEdit = QtWidgets.QLineEdit(registrationWindow)
        self.lastNameLineEdit.setGeometry(QtCore.QRect(240, 160, 460, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.lastNameLineEdit.setFont(font)
        self.lastNameLineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lastNameLineEdit.setTabletTracking(True)
        self.lastNameLineEdit.setStyleSheet("border-color: rgb(0, 85, 0);")
        self.lastNameLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lastNameLineEdit.setObjectName("lastNameLineEdit")
        self.firstNameLineEdit = QtWidgets.QLineEdit(registrationWindow)
        self.firstNameLineEdit.setGeometry(QtCore.QRect(240, 280, 460, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.firstNameLineEdit.setFont(font)
        self.firstNameLineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.firstNameLineEdit.setTabletTracking(True)
        self.firstNameLineEdit.setStyleSheet("border-color: rgb(0, 85, 0);")
        self.firstNameLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.firstNameLineEdit.setObjectName("firstNameLineEdit")
        self.loginLineEdit = QtWidgets.QLineEdit(registrationWindow)
        self.loginLineEdit.setGeometry(QtCore.QRect(240, 400, 460, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.loginLineEdit.setFont(font)
        self.loginLineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.loginLineEdit.setTabletTracking(True)
        self.loginLineEdit.setStyleSheet("border-color: rgb(0, 85, 0);")
        self.loginLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.loginLineEdit.setObjectName("loginLineEdit")
        self.passwordLineEdit = QtWidgets.QLineEdit(registrationWindow)
        self.passwordLineEdit.setGeometry(QtCore.QRect(240, 510, 460, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.passwordLineEdit.setTabletTracking(True)
        self.passwordLineEdit.setStyleSheet("border-color: rgb(0, 85, 0);")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.inputButton = QtWidgets.QPushButton(registrationWindow)
        self.inputButton.setGeometry(QtCore.QRect(370, 600, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.inputButton.setFont(font)
        self.inputButton.setStyleSheet("")
        self.inputButton.setDefault(False)
        self.inputButton.setFlat(False)
        self.inputButton.setObjectName("inputButton")
        self.backButton = QtWidgets.QPushButton(registrationWindow)
        self.backButton.setGeometry(QtCore.QRect(10, 20, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("")
        self.backButton.setDefault(False)
        self.backButton.setFlat(False)
        self.backButton.setObjectName("backButton")

        self.backButton.clicked.connect(backWindowShow)
        self.inputButton.clicked.connect(lambda: testParam(self.firstNameLineEdit.text(), self.lastNameLineEdit.text(),
                                                           self.loginLineEdit.text(), self.passwordLineEdit.text()))
        self.retranslateUi(registrationWindow)
        QtCore.QMetaObject.connectSlotsByName(registrationWindow)

    def retranslateUi(self, registrationWindow):
        _translate = QtCore.QCoreApplication.translate
        registrationWindow.setWindowTitle(_translate("registrationWindow", "Dialog"))
        self.startLabel.setText(_translate("registrationWindow", "Регистрация"))
        self.lastNameLabel.setText(_translate("registrationWindow", "Введите фамилию:"))
        self.firstNameLabel.setText(_translate("registrationWindow", "Введите имя:"))
        self.loginLabel.setText(_translate("registrationWindow", "Введите логин:"))
        self.passLabel.setText(_translate("registrationWindow", "Введите пароль:"))
        self.lastNameLineEdit.setPlaceholderText(_translate("registrationWindow", "Пример: Иванов"))
        self.firstNameLineEdit.setPlaceholderText(_translate("registrationWindow", "Пример: Иван"))
        self.loginLineEdit.setPlaceholderText(_translate("registrationWindow", "Пример: ivanov_ivan"))
        self.passwordLineEdit.setPlaceholderText(_translate("registrationWindow", "Пример: 1234"))
        self.inputButton.setText(_translate("registrationWindow", "Войти"))
        self.backButton.setText(_translate("registrationWindow", "Назад"))


def testParam(firstName, lastName, login, password):
    from InputTest import registrationParamTest
    registrationParamTest(lastName, firstName, login, password)


def backWindowShow():
    from QtWindows.authorizationWindow import showAuthorizationWindow
    showAuthorizationWindow()
    closeRegistrationWindow()


def showRegistrationWindow():
    global registrationWindow
    registrationWindow = QtWidgets.QDialog()
    ui = Ui_registrationWindow()
    ui.setupUi(registrationWindow)
    registrationWindow.show()


def closeRegistrationWindow():
    registrationWindow.close()