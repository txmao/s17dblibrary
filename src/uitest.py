'''
Created on Mar 5, 2017
for testing of ui
@author: mdy
'''

import sys
from PyQt4 import QtCore, QtGui, uic

myqtfile = 'UI/myui1.ui'

Ui_MainWindow, QtBaseClass = uic.loadUiType(myqtfile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Search_Button.clicked.connect(self.iop)
        #self.Show_Table.setColumnCount(4)
        
    def iop(self):
        p = self.Search_Box.toPlainText()
        self.test_my.setText(p)
        self.Show_Table.setColumnCount(4)
        #self.Show_Table.setText(p)
        
if __name__=='__main__':
    ap = QtGui.QApplication(sys.argv)
    wd = MyApp()
    wd.show()
    sys.exit(ap.exec_())
        
        
        
