# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projecttwo.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_otherWindow(object):
    def setupUi(self, otherWindow):
        otherWindow.setObjectName("otherWindow")
        otherWindow.resize(559, 478)
        self.centralwidget = QtWidgets.QWidget(otherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 390, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 10, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        otherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(otherWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 559, 20))
        self.menubar.setObjectName("menubar")
        otherWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(otherWindow)
        self.statusbar.setObjectName("statusbar")
        otherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(otherWindow)
        QtCore.QMetaObject.connectSlotsByName(otherWindow)

    def retranslateUi(self, otherWindow):
        _translate = QtCore.QCoreApplication.translate
        otherWindow.setWindowTitle(_translate("otherWindow", "MainWindow"))
        self.pushButton.setText(_translate("otherWindow", "EXIT"))
        self.label.setText(_translate("otherWindow", "ESSAY DETAILS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    otherWindow = QtWidgets.QMainWindow()
    ui = Ui_otherWindow()
    ui.setupUi(otherWindow)
    otherWindow.show()
    sys.exit(app.exec_())