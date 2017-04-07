# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myui1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Library_MainWindow(object):
    def setupUi(self, Library_MainWindow):
        Library_MainWindow.setObjectName(_fromUtf8("Library_MainWindow"))
        Library_MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(Library_MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Search_Box = QtGui.QTextEdit(self.centralwidget)
        self.Search_Box.setGeometry(QtCore.QRect(20, 10, 341, 31))
        self.Search_Box.setObjectName(_fromUtf8("Search_Box"))
        self.Search_Button = QtGui.QPushButton(self.centralwidget)
        self.Search_Button.setGeometry(QtCore.QRect(370, 10, 99, 27))
        self.Search_Button.setObjectName(_fromUtf8("Search_Button"))
        self.Show_Table = QtGui.QTableWidget(self.centralwidget)
        self.Show_Table.setGeometry(QtCore.QRect(20, 50, 661, 271))
        self.Show_Table.setObjectName(_fromUtf8("Show_Table"))
        self.Show_Table.setColumnCount(0)
        self.Show_Table.setRowCount(0)
        self.test_my = QtGui.QTextEdit(self.centralwidget)
        self.test_my.setGeometry(QtCore.QRect(690, 170, 104, 78))
        self.test_my.setObjectName(_fromUtf8("test_my"))
        Library_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Library_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Library_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Library_MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Library_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(Library_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Library_MainWindow)

    def retranslateUi(self, Library_MainWindow):
        Library_MainWindow.setWindowTitle(_translate("Library_MainWindow", "Library_S17", None))
        self.Search_Button.setText(_translate("Library_MainWindow", "Search", None))

